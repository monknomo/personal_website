Title: Map in a Java Stream, What is it?
Slug: map-in-java-stream
Date: 6/13/2018 07:00
Modified: 6/13/2018 07:00
Category: Programming
Tags: java, functional, fp, java8
Authors: Gunnar Gissel
Summary: Working with streams often requires 'mapping' of objects.  What is mapping, and why do people do it with streams?
cover_image: https://thepracticaldev.s3.amazonaws.com/i/rxu7unjfnzoutafucx6q.png

Mapping is how to convert one type of object to another with a stream.  Say you have a set of `Fruit` and you want to show people what is in your set.  It would be helpful to have a list of fruit names to do so.

    fruitList.stream().map(fruit -> fruit.getName()).collect(Collectors.asList);

That's pretty simple; you can imagine how to do that in real life with a basket of fruit.  

Pick up a piece of fruit, write its name down.  Pick up another piece of fruit, write its name down, etc.

Mapping also lets you you can't easily simulate in real life.  Say you have a Fruit set and you want Oranges, instead of Apples (I think this is closer to transmutation than swapping, but it's a metaphor, ymmv).

You can do that, with Java:

    fruitList.stream().map(fruit -> {
        if( fruit instanceof Apple){
            return new Orange();
        }
        return  fruit;
    }).collect(Collectors.asSet);

Have fun out there, and map all the things!
