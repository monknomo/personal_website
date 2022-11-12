Title: Turn Your Spaghetti Code into Functions - Part 2
Slug: turn-your-spaghetti-code-into-functions-part-2
Date: 9/7/2017 06:00
Modified: 9/7/2017 06:00
Category: Programming
Tags: java, technique, diy, how-to, tutorial, guide, lambda, function, refactor
Authors: Gunnar Gissel
Summary: How Predicates can help clean your code, and how to start using them

Read [Part 1,](http://www.gunnargissel.com/turn-your-spaghetti-code-into-functions-part-1.html) first.

In Part 1, we started with [an example of common business logic code,](https://github.com/monknomo/If-Else-Block-Refactoring/blob/master/src/main/java/com/gunnargissel/suemez/businessrulerefactorexample/BusinessRulesEngine.java) and an analogy based on cramming an elephant into a Smart Car. We did some refactoring to untangle the nested if/else blocks, but we left after we finished cramming the elephant into a Smart Car.

<img src="https://i.imgur.com/xfmb1Bs.png"  title="An elephant driving a Smart Car"/>

In many ways, it feels "good enough", but what if I told you we can get it better?  Java 8 brings us a new tool to contain and use the logic within an `if` statement - the Predicate.  In terms of elephants driving cars, we can get it driving a stylish convertible.

So you have a lot of conditional logic, and you find yourself copy-pasting conditions from one logic block to the other.  It's easy, it's seductive, but it's wrong.  Copy pasting is error prone and extra work!  If you're like me, you try to work as little as possible - that's the computer's job.  Java 8 provides a new tool to prevent copy-pasting and keep your code [DRY.](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

Using Predicates allows us to encapsulate logic as a variable.  This makes for two features that are particularly powerful

1. Variable names communicate the intent of the logic
2. Logic is resusable and individually testable

And Now, With Predicates
-------------------------

Before Java 8, I wasn't tuned in to the functional programming world.  The last time I remember hearing about Predicates was in school when I was ignoring a grammar lesson.  It turns out that, when programming, Predicates can really improve your code.

<img src="https://i.imgur.com/jgs74pKm.jpg" title="A grammar school" alt="A grammar school" />

Here we will make the `if/else` blocks more readable by creating Predicates out of the logic they represent.  Predicates can be named, which allows developers to name rules in a way that allows for clear discussions with even non-technical users.

    static final Predicate<WidgetTransfer> suffientAmount = trans -> trans.getTransferer().getAccount(trans.getFromAccount()).getBalance().compareTo(trans.getAmount()) > 0;
    static final Predicate<String> isPartner = ttc -> ttc.equals("200");
    static final Predicate<String> isFriendsAndFamily = ttc -> ttc.equals("710");
    static final Predicate<String> isFriendAndFamilyDiscountLegal = ac -> ac.matches("574|213|363|510");
    static final Predicate<String> isPartneringArea = ac -> ac.matches("907|412|213");
    static final Predicate<String> isDirigibleArea = ac -> ac.matches("213");
    static final Predicate<String> isDirigibleCategory = cat -> cat.equals("D");
    static final Predicate<String> isInternal = tc -> tc.equals("I");

    public static final String checkWidgetTransfer(WidgetTransfer transfer) {
        String businessRuleErrors = "";

        String transferTypeCode = transfer.getTransferTypeCode();
        String areaCode = transfer.getAreaCode();
        String category = transfer.getTransferer().getCategory();
        String typeCode = transfer.getTypeCode();

        if (suffientAmount.test(transfer)) {
            businessRuleErrors += "Insufficient balance to transfer ; ";
        }

        if (isPartner.test(transferTypeCode)
                && isPartneringArea.negate().test(areaCode)) {
            businessRuleErrors += "This area is not a transfer eligible area. ; ";
        }

        if (isPartner.test(transferTypeCode)
                && isDirigibleArea.test(areaCode)
                && isDirigibleCategory.test(category)) {
            businessRuleErrors += "D Category Transferer can only be transferred in transfer area 213. ; ";
        }

        if (isFriendsAndFamily.test(transferTypeCode)
                && isFriendAndFamilyDiscountLegal.negate().test(areaCode)) {
            businessRuleErrors += "This area is not an eligible area. ; ";

        }

        if (isInternal.negate().test(typeCode)
                && !isBlockSize(transfer)) {
            businessRuleErrors += "Amount is too small for I type transfer. ; ";
        }

        if (isInternal.negate().test(typeCode)
                && isTotalOverCap(transfer)) {
            businessRuleErrors += "This transfer is too large. ; ";
        }

        return businessRuleErrors;
    }

### The Good

* Each `if` block is readable in something approximating "business English"
* The rules are defined as Predicates
  *  The rules are portable and reusable.
  * The rules are also individually testable, without having to test each branch at once

### The Bad

* This technique still uses `&&` which is not idiomatic with functions in Java
  * We are forced to use `&&` because the Predicates take different types of objects, so we can't chain them together
* While the Predicates that make up the rules are portable, the rules themselves are made of multiple Predicates and are not portable
* Nothing has been done that can't be done with ordinary methods
  * Good old `public boolean isSufficientAmount(String amount)` would suffice
* We still have to create all these property variables to get the appropriate values to give to our Predicates

Predicate Chaining
---------------------

Let's fix some of the stuff on the 'bad' list from the previous example.  

We can get rid of `&&` by using just a little bit more of the functional interface and refactoring the Predicates to all take the same type of object, in this case a `WidgetTransfer` object.  The goal is to make our Predicates like legos - interlocking and interchangeable.

<img src="https://i.imgur.com/OfJVe6hm.jpg" title="lego elephant" alt="lego elephant"/>

    static final Predicate<WidgetTransfer> suffientAmount = trans -> trans.getTransferer().getAccount(trans.getFromAccount()).getBalance().compareTo(trans.getAmount()) > 0;
    static final Predicate<WidgetTransfer> isPartner = trans -> trans.getTransferTypeCode().equals("200");
    static final Predicate<WidgetTransfer> isFriendsAndFamily = trans -> trans.getTransferTypeCode().equals("710");
    static final Predicate<WidgetTransfer> isFriendAndFamilyDiscountLegal = trans -> trans.getAreaCode().matches("574|213|363|510");
    static final Predicate<WidgetTransfer> isPartneringArea = trans -> trans.getAreaCode().matches("907|412|213");
    static final Predicate<WidgetTransfer> isDirigibleArea = trans -> trans.getAreaCode().matches("213");
    static final Predicate<WidgetTransfer> isDirigibleCategory = trans -> trans.getTransferer().getCategory().equals("D");
    static final Predicate<WidgetTransfer> isInternal = trans -> trans.getTypeCode().equals("I");
    static final Predicate<WidgetTransfer> isBlockSize = trans -> isBlockSize(trans);
    static final Predicate<WidgetTransfer> isTotalOverCap = trans -> isTotalOverCap(trans);

    public static final String checkWidgetTransfer(WidgetTransfer transfer) {
        String businessRuleErrors = "";

        if (suffientAmount.test(transfer)) {
            businessRuleErrors += "Insufficient balance to transfer ; ";
        }

        if (isPartner.and(isPartneringArea.negate()).test(transfer)) {
            businessRuleErrors += "This area is not a transfer eligible area. ; ";
        }

        if (isPartner.and(isDirigibleArea).and(isDirigibleCategory).test(transfer)) {
            businessRuleErrors += "D Category Transferer can only be transferred in transfer area 213. ; ";
        }

        if (isFriendsAndFamily.and(isFriendAndFamilyDiscountLegal.negate()).test(transfer)) {
            businessRuleErrors += "This area is not an eligible area. ; ";
        }

        if (isInternal.negate().and(isBlockSize.negate()).test(transfer)) {
            businessRuleErrors += "Amount is too small for I type transfer. ; ";
        }

        if (isInternal.negate().and(isTotalOverCap.negate()).test(transfer)) {
            businessRuleErrors += "This transfer is too large. ; ";
        }

        return businessRuleErrors;
    }

### The Good

* We get rid of extra variables that hold string values from the `WidgetTransfer` object
* We compact our `if`-blocks while retaining readability
* We only evaluate one type of object


### The Bad

There is very little bad about this refactor point.  The conditionals are all very easy to read.  It's clear what each rule is, and what branch.  If I didn't know what I have planned for the next article, I would be satisfied to stop here.

Next Steps
------------

<img src="https://i.imgur.com/N5Xf1IBl.png" title="elephant driving a convertible citroen" alt="elephant driving a convertible citroen" />

All our rules are Predicates and each rule takes the same kind of object, a `WidgetTransfer`.  That makes our rule composable in the fashion demonstrated above, but there are some improvements we can make to how we compose the business rules.

The first improvement is to combine small rules into larger rules - we are doing this in conditional statements, but it is just as easy to do so in a Predicate.  We can also create a `Validator` object to create a collection of business rules and error messages.  A `Validator` dispenses with the need to create a complex nested if/else logic structure, and is a concrete unit of business logic that can be shared, re-used and tested.

[Sign up for my email list to get notifcations about updates in continuing series, and a monthly digest of interesting programming and tech leadership articles](http://www.gunnargissel.com/pages/email-signup-1.html)

We will go over using `Validators` in the to-be-written _Turn Your Spaghetti Code into Functions, Part III_

## Credits

_Thank you [roebot](https://www.flickr.com/photos/roebot/) for the [left facing Smart Car](https://flic.kr/p/73uXD3)_

_Thank you [Oliver Dodd](https://www.flickr.com/photos/oliverdodd/) for the [elephant](https://flic.kr/p/8N681r)_

_Thank you [Phillip Pessar](https://www.flickr.com/photos/southbeachcars/) for the [convertible](https://flic.kr/p/dvLhLi)_

_Thank you JPL and NASA/Space Telescope Science Institute for the edge-on galaxy picture_

_Thank you [Philip Sheldrak](https://www.flickr.com/photos/philip_sheldrake/) for the [grammar school](https://flic.kr/p/8AaePC)_
