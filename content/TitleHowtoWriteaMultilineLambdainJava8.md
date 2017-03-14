Title: How to Write a Multiline Lambda in Java 8
Slug: how-to-write-a-multiline-lambda-in-java8
Date: 3/13/2017 12:00
Modified: 3/13/2017 12:00
Category: Programming
Tags: how-to, tutorial, guide, functional-programming, java8
Authors: Gunnar Gissel
Summary: A short example of how to make multiline lambda functions in Java 8


For the most part, single line lambda functions are all you need.


This is a single line lambda:


    Predicate<String> isBig = str -> str.length() > 10;


Sometimes one line is not enough to express the complexity of the lambda.  How do you make a multiline lambda?


This is how:


    Predicate<Animal> isDog = animal -> {
        try {
            return barks.test(animal.getSound()) &&
            wagsTail.test(animal);
        } catch (MuteAnimalException e){
            logger.severe(e.getMessage);
            return false;
        }
    };