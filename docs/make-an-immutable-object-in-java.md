Title: Make an Immutable Object - in Java
Slug: make-an-immutable-object-in-java
Date: 6/4/2018 18:00
Modified: 6/4/2018 18:00
Category: Programming
Tags:  java, fp, design, tips 
Authors: Gunnar Gissel
Summary: How to make an immutable object, in Java.  Including common gotchas, design pattern considerations and what to do with bad data.
cover_image: https://thepracticaldev.s3.amazonaws.com/i/hp1iz5pl5a2c4eakl6qa.png
author_facebook_id: gunnar.gissel
facebook_app_id: 962146893962636
author_twitter: monknomo

<a name="making-an-immutable-object"></a>
Immutable objects are objects that don't change.  You make them, then you can't change them.  Instead, if you want to change an immutable object, you must clone it and change the clone while you are creating it.

A Java immutable object must have all its fields be internal, `private final` fields.  It must not implement any setters.  It needs a constructor that takes a value for every single field.

Immutable objects come in handy in multi-threaded environments and in streams.  It is great to rely on objects not changing mid-stream.  Bugs caused by a thread changing another thread's object are often subtle and are very, _very_ hard to track down.  Immutable objects stop these whole class of problems in their tracks.

You don't have to take my word for it - see what [experts](https://www.yegor256.com/2014/06/09/objects-should-be-immutable.html) [around](https://www.codebetter.com/patricksmacchia/2008/01/13/immutable-types-understand-them-and-use-them/) [the](https://www.codebetter.com/patricksmacchia/2008/01/13/immutable-types-understand-them-and-use-them/) [web](https://stackoverflow.com/questions/214714/mutable-vs-immutable-objects) say.

Contents
----------

1. [Making an Immutable Object](#making-an-immutable-object)
1. [Common gotchas](#gotchas)
    1. [Primitives](#primitive-gotchas)
    1. [Collections](#collections-gotchas)
    1. [Arrays](#array-gotchas)
    1. [Objects](#object-gotchas)
1. [How to Change an Immutable Object](#how-to-change-an-immutable-object)
    1. [Where to put Builders?](#where-to-put-builder-objects)
1. [Handling Bad Data in Immutable Objects](#handle-bad-data)
1. [Wrapup](#wrapup)

Gotchas!<a name="gotchas"></a>
---------

<img src="https://i.imgur.com/51q4QPRl.jpg" title="a lonely tree on a rock" alt="a lonely tree on a rock"/>

Lists, arrays, maps, sets and other non-immutable objects can be surprising.  A `private final` object with no setter is fixed to the object it was initially assigned, but the values inside that object aren't fixed (unless the object is immutable).

That means you might have an `ImmutableShoppingList myShoppingList = new ImmutableShoppingList(new String[] {"apples","anchovies","pasta"})` and expect that the shopping list will always have "apples", "anchovies" and "pasta".

Someone could call `myShoppingList.getList()[0] = "candy bars";` and change your list to be "candy bars", "anchovies" and "pasta", which is unhealthy and clearly not what you want.

### Primitives <a name="primitive-gotchas"></a>

Good news!  Primitives are immutable, so you don't have to do anything special. 

### Collections <a name="collections-gotchas"></a>

Good news! [java.util.Collections](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html) provides a number of convenience methods that make converting a Collection to an UnmodifiableCollection a snap.

Check out:

    Collections.unmodifiableCollection
    Collections.unmodifiableList
    Collections.unmodifiableMap
    Collections.unmodifiableNavigableMap
    Collections.unmodifiableNavigableSet
    Collections.unmodifiableSet
    Collections.unmodifiableSortedMap
    Collections.unmodifiableSortedSet

I suggest you store the fields as generic Collections (List, rather than ArrayList), and make the unmodifiable in the constructor, like so:


    public class ImmutableShoppingList {
    
        private final List<String> list;
    
        public ImmutableShoppingList(List<String> list){
            this.list = Collections.unmodifiableList(list);
        }
    
        public List<String> getList(){
            return list;
        }
    }

This allows you to use IDE code generation to make the getters, which is nice, and contains all the input modifiers in one place, which is also nice.

Bad news! If you hang onto the reference to the collection when you create the collection, you can still modify it, even if you store it as an unmodifiable collection internally.  Here's an example:

    List<String> originalList = new ArrayList<>();
    theList.add("apple");
    ImmutableShoppingList blah = new ImmutableShoppingList(originalList);
    originalList.add("candy bar");

The supposedly immutable shopping list started with an apple, and had a candy bar added to it after creation.  What can we do about this?

Clone the list!

    public class ImmutableShoppingList {

        private final List<String> list;

        public ImmutableShoppingList(List<String> list){
            List<String> tmpListOfHolding = new ArrayList<>();
            tmpListOfHolding.addAll(list);
            this.list = Collections.unmodifiableList(tmpListOfHolding);
        }

        public String[] getList(){
            return (String[]) list.toArray();
        }
    }

When we create the immutable object, we deep clone the collection, which severs the connection to the original reference.  Now when we run the "sneak a candy bar in" example, "candy bar" gets added to `originalList`, but not the `ImmutableShoppingList`.

### Arrays <a name="array-gotchas"></a>

Bad news!  Java doesn't have any convenient methods to prevent arrays from being modified.  Your best bet is to either hide the original array and always return a clone, or to not use arrays in the underlying implementation and instead convert a Collection object to an array.

I prefer to stick with Collections, but if you must have an array in your object's api, this is the approach I would take:

    public class ImmutableShoppingList {

        private final List<String> list;

        public ImmutableShoppingList(String[] list){
            this.list = Collections.unmodifiableList(Arrays.asList(list));
        }

        public String[] getList(){
            return (String[]) list.toArray();
        }
    }

### Objects <a href="object-gotchas"></a>

Object fields can be easy.  If the sub-objects are also immutable, good news!  You don't have to do anything special.

If the sub-objects are not immutable, they are a lot like a collection.  You need to deep clone them, or the original reference can change your supposedly immutable data out from under your feet.

Often, you end up working with pre-existing mutable objects, either in your codebase, or in libraries.  In this case, I like to create an immutable object wrapper class that _extends_ the mutable class.  I find a static `getInstance(MutableObject obj)` method can be helpful, but a constructor `ImmutableObject(MutableObject obj)` is also a useful thing to have.

What About When I Want To Change An Immutable Object? <a name="how-to-change-an-immutable-object"></a>
----------------------------------------------------------

<img src="https://i.imgur.com/IHsv75ol.jpg" title="a woman having a good time in a shop" alt="a woman having a good time in a shop"/>

It happens to everyone.  You need an an object, but you don't know everything about the object.  You can't quite commit to an immutable object.

In this case, I reach for the builder pattern.

The builder pattern creates a temporary object with the same fields as the desired object.  It has getters and setters for all the fields.  It also has a `build()` method that creates the desired object

Imagine a small immutable object:

    class ImmutableDog {
        private final String name;
        private final int weight

        public ImmutableDog(String name, int weight){
            this.name = name;
            this.weight = weight;
        }

        public String getName(){
            return this.name;
        }

        public int getWeight(){
            return this.weight;
        }
    }


Here's what the builder would look like:

    class ImmutableDogBuilder {
        private String name;
        private int weight;

        public ImmutableDogBuilder(){}

        public ImmutableDog build(){
            return new ImmutableDog(name, weight);
        }

        public ImmutableDogBuilder setName(String name){
            this.name = name;
            return this;
        }

        public ImmutableDogBuilder setWeight(int weight){
            this.weight = weight;
            return this;
        }

        public String getName(){
            return this.name;
        }

        public int getWeight(){
            return this.weight;
        }
    }

__Note the setters__  I really like this pattern of returning `this` on each setters in builder classes, because it creates a very fluent api.  You could use this `ImmutableDogBuilder` like this:

    ImmutableDogBuilder dogBuilder = new ImmutableDogBuilder().setName("Rover").setWeight(25);

You can imagine in classes with more fields that this compacts your code a lot.

### Where To Put The Builder? <a name="where-to-put-builder-objects"></a>

There are two schools of thought here.

On the one hand, you can create a separate class for the builder.  This is easy, it is very conventional, and your IDE will probably group the classes together, because they probably have similar names.

On the other hand, you can embed the builder class in the immutable object class as a public static inner class.

I prefer to embed builder classes in immutable objects, because I view the builder as a helper for the immutable object, and not a standalone thing.  It keeps them together and tightly coupled.

What About Immutable Objects With Bad Data? <a name="handle-bad-data"></a>
---------------------------------------------

<img src="https://i.imgur.com/cqrtgTXl.jpg" title="a very dirty car" alt="a very dirty car"/>

It happens to everybody, especially if you accept input.  Bad data!

Bad data is no good, but _immutable_ bad data seems especially wrong - you can't even fix it!

I use two approaches to prevent bad data from getting turned into immutable objects.

My primary approach is a suite of business rules that test for sane, permissible data.  The business rules look at builders, and if the builder passes, I deem it ok to create the immutable object.

My secondary approach is to embed a small amount of business logic in the immutable object.  I don't allow required fields to be null, and any nullable field is an `Optional`.

For example:

    class ImmutableDog {
        private final String name;
        private final Optional<int> weight

        public ImmutableDog(String name, Optional<int> weight){
            Objects.requireNonNull(name);
            this.name = name;
            this.weight = weight;
        }

        public String getName(){
            return this.name;
        }

        public Optional<int> getWeight(){
            return this.weight;
        }
    }

This is an `ImmutableDog` that requires a name, but does not require a weight.  It's important to know what to call a dog, but it's not strictly necessary to know that Fluffy weighs 15 lbs.

`Objects.requireNonNull` will immediately throw a `NullPointerException` if a name is not provided.  This prevents the creation of a nonsensical immutable object.  It also allows users of the immutable object (such as streams or functions) to skip handling nulls.  There are no nulls here.

Using `Optional<int>` makes consumers of `ImmutableDog` immediately aware that they may have to handle a null.  Providing the `Optional` api gives downstream users an easy, functional way of handling nulls.

Wrapup <a name="wrapup"></a>
--------------------------------

<img src="https://i.imgur.com/fiWbSvbl.jpg" title="a colorful celebration" alt="a colorful celebration"/>

Immutable objects require some special care and handling, but their utility is worth it.

The main principles to keep in mind are:

1. Clone arrays, Collections and Objects internal to your immutable object
2. Use builders when you need a mutable object
3. Use Optional to indicate nullable fields in your object's api
4. Fail fast on bad data - Objects.requireNonNull can help

Go forth, and stop mutating
