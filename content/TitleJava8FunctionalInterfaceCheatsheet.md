Title: Java 8 Functional Interface Cheatsheet
Slug: java8-functional-interface-cheatsheet
Date: 3/13/2017 18:00
Modified: 3/13/2017 18:00
Category: Programming
Tags: cheatsheet, how-to, guide, tutorial, functional-programming, java8
Authors: Gunnar Gissel
Summary: A cheatsheet for developing with the Java 8 functional interfaces


[O'Reilly has a great in-depth article on the functional interface in Java 8.](https://www.oreilly.com/learning/java-8-functional-interfaces)  Here's a quick cheat sheet to keep track of the main types, what they do and common use cases.


`Predicate`
-------------


A `Predicate` returns true or false.  These are used for filters or replacing big chains of if/else logic.


`Function`
-------------


A `Function` transforms data.  These are used for maps, and other transformations.  It is important to not mutate the original data that is passed in.


`Supplier`
-------------


A `Supplier` takes no arguments and returns a value of a known type.  Fetching, reading or creating resources to be used by other functions are common use cases.  Suppliers get things started.


`Consumer`
--------------


A `Consumer` accepts a single argument, but does not return any results.  Consumers are where mutating functions, things with side-effects, should go.  Consumers finish things.