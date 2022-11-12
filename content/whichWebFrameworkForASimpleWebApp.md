Title: Which Framework is Best for a Simple Web App?
Date: 03/09/2016 20:15
Modified: 03/09/2016 20:15
Category: Operations
Tags: java, web, servlet, framework
Slug: how-to-build-a-simple-web-app-in-java
Author: Gunnar Gissel
Email: monknomo@gmail.com
Summary: Choose the most straightforward way to make a web application in Java


Lots of people want to wet their feet with web development by building with Java.  The trouble is that Java presents an overwhelming number of frameworks.  It's easy to go round and round in circles, stuck in analysis paralysis.  They read about JavaEE, then servlets.  Someone on a forum says Spring is better.  A flamewar erupts between Play and Grails.

What *should* a person do?

I think the most important thing to do, when faced with overwhelming choices, is to pause and step back. Take a deep breath!  Go for a walk away from the computer.  When you come back, dig into what your intent really is.  In this case, you want to make a simple web app.  "Hello world" in Java, but on the web.

I suggest choosing the simplest option, which is vanilla Java servlets.  Don't bother with a framework until you know the application is complex enough be worth the overhead.  After you've made your simple servlet, build a war, deploy it to Tomcat and call it a day.

That said, if you must use a framework...

Use Dropwizard
=================

Java has a reputation for being [heavyweight and verbose](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition).  It doesn't have to be that way.  [Dropwizard](www.dropwizard.io/) takes a lot of verbosity and enterprise-yness out of making a web application (especially compared to Spring).  I'm a fan, and if you're hellbent on using a framework, try out Dropwizard.