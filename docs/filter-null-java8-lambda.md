Title: Filter Null Value from a List with Java8 Lambda
Slug: filter-null-value-from-list-with-java8-lambda
Date: 6/8/2018 16:30
Modified: 6/8/2018 16:30
Category: Programming
Tags: java, fp, functional-programming, java8, lambda, stream
Authors: Gunnar Gissel
Summary: Filter nulls from Collections easily with Java 8 Lambdas and the Stream api!
cover_image: https://thepracticaldev.s3.amazonaws.com/i/u9bya8rdc3cs7o2mpc9f.png

A common task with Java streams is to clean up the input data so later steps can work without thinking too hard.  Likely the #1 most common cleanup step is to remove nulls from a Collection.

Streams make it easy:

    myCollection.stream()
      .filter(Objects::nonNull)
      .do.what.you.need

Compare with the classic approaches:

    while(myCollection.remove(null));
    // do what you need, but you better not need that original list, because it's gone...
    myCollection.removeAll(Collections.singleton(null));
    // do what you need, but you better not need that original list, because it's gone...

Like the stream approach, these are short and sweet, but unlike the stream approach they modify the original list.  The first example is also pretty slow.

I like the stream approach because I can chain additional tasks after the filter task, including `map`. `sorted`, `reduce` and more!.  I find the traditional imperative iterative approach to be not only wordier, but conceptually harder to follow.
