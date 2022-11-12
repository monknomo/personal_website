Title: Finding Null or Empty String Checks in Java
Slug: finding-null-or-empty-string-checks-in-java
Date: 5/11/2017 21:00
Modified: 5/11/2017 21:00
Category: Programming
Tags: java, praxis, practices, java8, functions, regex
Authors: Gunnar Gissel
Summary: I wrote a regex that finds many forms of checks for null or empty strings in Java, so I could replace them with a Predicate


I have a lot of code like this:


    if( null == myString || "".equals(myString))
        doAThing();


The codes fine, really.  Very idiomatic, gets the job done.


Lately, I've been on a predicate kick.  I like replacing my conditionals with predicates that describe the intent of the conditional statement.  I can also replace a lot of my boilerplate code with a couple common predicates.  This is one I use a lot:


     public static final Predicate<String> NULL_OR_EMPTY = (in) -> null==in || "".equals(in);


It's true; if the code base had been crafted with Optionals or other null-avoidance techniques, that I could mostly ignore this check.  My code base has history and weight and external interfaces, so there are plenty of this check and others like it.


I have been using [this regex](regexr.com/3fu2e) to find likely places that I can apply my predicate:


      /\(\s*null\s*==\s*(\S*)\s*\|\|\s*""\.equals\(\s*\1\s*\)\s*\)|\(\s*(\S*)\s*==\s*null\s*\|\|\s*""\.equals\(\s*\2\s*\)\s*\)|\(\s*null\s*==\s*(\S*)\s*\|\|\s*\3\.equals\(\s*""\s*\)\s*\)|\(\s*(\S*)\s*==\s*null\s*\|\|\s*\4\.equals\(\s*""\s*\)\s*\)|\(\s*""\.equals\(\s*(\S*)\s*\)\s*\|\|\s*null\s*==\s*\5\s*\)|\(\s*(\S*)\.equals\(\s*""\s*\)\s*\|\|\s*null\s*==\s*\6\s*\)|\(\s*""\.equals\(\s*(\S*)\s*\)\s*\|\|\s\7\s*==\s*null\s*\)|\(\s*(\S*).equals\(\s*""\s*\)\s*\|\|\s*\8\s*==\s*null\s*\)|\(\s*null\s*==\s*(\S*)\s*\|\|\s*""\s*==\s*\9\s*\)|\(\s*(\S*)\s*==\s*null\s*\|\|\s*""\s*==\s*\10\s*\)|\(\s*null\s*==\s*(\S*)\s*\|\|\s*\11\s*==\s*""\s*\)|\(\s*(\S*)\s*==\s*null\s*\|\|\s*\12\s*==\s*""\s*\)|\(\s*""\s*==\s*(\S*)\s*\|\|\s*null\s*==\s*\13\s*\)|\(\s*(\S*)\s*==\s*""\s*\|\|\s*null\s*==\s*\14\s*\)|\(\s*""\s*==\s*(\S*)\s*\|\|\s*\15\s*==\s*null\s*\)|\(\s*(\S*)\s*==\s*""\s*\|\|\s*\16\s*==\s*null\s*\)/g


It's an ugly one, but it matches a lot of common patterns for checking if a string is null or empty.  I'm hopeful that folks will suggest either a better way of finding null or empty checks or help me add to my hideous regex!