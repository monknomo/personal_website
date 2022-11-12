Title: Java 8 Stream Cheatsheet
Slug: java8-stream-cheatsheet
Date: 02/28/2018 07:00
Modified: 02/28/2018 07:00
Category: Programming
Tags: java8, programming, cheatsheet, guide, how-to, tutorial
Authors: Gunnar Gissel
Summary: A cheatsheet that organizes and describes the most useful methods for working with Java 8 streams

Streams are a way of working with objects in a collection.

Streams allow a person to say what they _want_ to have at the end.  Contrast that with the imperative approach that requires a person to say _how_ to collect what they want to have at the end.

Streams also allow for trivial multi-threading.

Basic Stream Methods
=====================

There are a couple basic methods that govern stream interaction.  The general idea behind these methods is manipulating a collection of objects so that the only objects remaining are the ones you want.

If I had to pick the indispensable methods for working with a Stream, I'd say `Map`, `Filter`, and `Collect` are on it.

__Filter__
Filter takes a `Predicate`, and leaves only the values that the `Predicate` is true for.

__Map__
Map takes a `Function`, and transforms the values in the stream from one type to another

__Sorted__
Sorted takes a `Comparator`, and orders the values in the stream according to the ordering specified in the `Comparator`.

__Collect__
`Collect` stops the stream and puts the values from the stream into some kind of `Collection`, like a `List`.

__toArray__
`toArray()` stops the stream and returns an array with the elements contained in the stream.

Finders
=========================================

A common task, when using a collection, is to get an element out of the stream.  These are generally used after `Filter` and `Map`, to guarantee that the element you find matches some criteria and is of the preferred type.

__findAny()__
`findAny()` returns an `Optional` containing an element in the stream (or nothing, if the stream is empty).  Order is not respected here, especially in parallel stream situations.

__findFirst()__
`findFirst()` returns an `Optional` containing the first element in the stream (or nothing, if the stream is empty).  Order is respected when using this method

__max(Comparator<T> comparator)__
`max` returns the maximum element of the stream for the given `Comparator`

__min(Comparator<T> comparator)__
`min` returns the minimum element of the stream for the given `Comparator`

Matchers
==========================================

Another common task is to determine if the objects meet some given criteria.  These "matcher" methods indicate whether some, none or all the objects in a stream meet a given criteria.

__allMatch(Predicate<T> pred)__
Returns `true` if all elements in the stream match the `Predicate`

__anyMatch(Predicate<T> pred)__
Returns `true` if any elements in the stream match the `Predicate`

__noneMatch(Predicate<T> pred)__
Returns `true` if no elements in the stream match the `Predicate`

Stream Modifiers
================

From time to time, a stream is not quite the "right" stream.  These methods create a new stream with slightly different characteristics than the old stream, whether it is a different length, different starting point, or a guarantee that only unique objects are contained.

__distinct()__
`distinct()` creates a new stream that has only distinct elements (based on `.equals`) in it

__limit(int maxSize)__
`limit(maxSize)` creates a new stream by truncating the original stream to be no longer than maxSize.

__skip(long n)__
Skips the first n elements of the stream, and creates a new stream out of the rest

__sorted()__
Creates a new stream, where the elements are sorted according to natural order

__sorted(Comparator<T> comparator)__
Creates a new stream, where the elements are sorted according to the `Comparator`


Stream Characterizers
======================

Another common task, when working with collections, is to determine some characteristics about the collection as a whole.  The stream api provides a method to figure out how big a given stream is.

__count()__
`count()` counts the number of elements in the stream

