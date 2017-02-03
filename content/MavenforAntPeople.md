Title: Maven for Ant People
Slug: maven-for-ant-people
Modified: 2/2/2016 19:00
Date: 2/2/2016 19:00
Category: Programming
Tags: maven, mvn, ant, java, build, tool, tools, tooling, beginner, how-to, walkthru, tutorial
Authors: Gunnar Gissel
Summary: Maven is great, but can be mystifying for Ant people


Ant people often find Maven completely mystifying.  I know I did.  I work at a shop that was, until recently, completely Ant based.  We built complex build scripts, and we did with XML, the way God Intended&trade;.


With Ant, you start from scratch.  You can have your project set up any way you want - the directory structure is up in the air, the artifacts you want to create through building are up in the air, you can even bring in conditionals to change the build based on whatever you want.  In short, Ant is the wild west.


Maven, by contrast, is a straightjacket.  Maven requires your projects are laid out in a particular way.  You have to use approved Maven directories, and you have to do things within the Maven lifecycle.  You can't just write a bunch of targets and stick them together any old way like you can with Ant.  Coming to a Maven project from the Ant world is very confusing, because the directory layout is slightly different, it isn't immediately obvious where dependencies are kept and when you try to run the pom as you would a build.xml, nothing happens.  Maven calls much of this behavior "convention over configuration" which makes things about as clear as mud.


Project Layout
===============


I think the first thing Ant people notice when they come to Maven is the directory structure is strange and different.  Most Ant projects I've worked in have a layout something like this:




    src/
    |- com/
       |- example/
          |- package/
            |- packageclass.java
            |- test/
               |- test.java
          |- otherpackage/
             |- otherclass.java
             |- test/
                |- testother.java
    deps/
    |- guava.jar
    |- jodatime.jar
    app.properties
    test.properties
    
Maven projects have a strict layout, like so:


    src/
    |- main/
       |- java/
          |- com/
             |- example/
                |- package/
                   |- packageclass.java
                |- otherpackage/
                   |- otherclass.java
       |- resources/
          |- app.properties
    |- test/
       |- java/
          |- com/
             |- example/
                |- package/
                   |- test.java
                |- otherpackage/
                   |- testother.java
       |- resources/
          |- test.properties
          
Maven expects code and resources to be in the `src` directory.  It further expects the `src` directory to contain a `main` and a `test` directory.  Things in the `main` directory are headed for the ultimate artifact.  Things in the `test` directory are test data, or junit tests, or other test code that we don't want to include in the ultimate artifact.


Both the `main` and `test` directories have `java` and optionally `resources` directories.  Java code goes in the `java` directory - this is assuming you are developing in Java, of course :)


Resources, like properties files, or test data, or FindBugs exclude files go in the `resources` directories.  If your project doesn't have any resources, you can dispense with these directories entirely.


The trick with Maven vs Ant is that Maven absolutely requires this directory structure.  It plain won't work without it.  At first, to my Ant eyes, that seemed needlessly constraining, but the more I've worked with it, the more I've liked it.  Any Maven project has the exact same directory structure, so as soon as you open a Maven project, you know where everything is, regardless of who developed it.  In my Ant shop, it helps to know who the first developer was, because each dev lays out a project slightly differently.  While this gives the code a charming old world village feel, it makes ramping up new devs a slow process.


Lifecycle
==========


Ant is made of build targets.  Targets are an xml element that define a unit of Ant behavior.  Targets can depend on other targets, so you can have some kind of order to your build.  You can define any number targets and call them whatever you want, and set up whatever hierarchy of targets makes sense to you.  


All that said, I think this might be a 'normal' structure for an Ant project:
    
    <project>
        <path></path>
        <target name="init"></target>
        <target name="compile" depends="init"></target>
        <target name="test" depend="compile"></target>
        <target name="jar" depend="test"></target>
        <target name="javadocs"></target>
    </project>
    
Reading over a Maven pom reveals no clues at all as to what the happens during the build.  Here's a schematic example to contrast with the Ant example above:


    <project>
        <meta stuff defining the project></meta stuff>
        <build></build>
        <dependencies></dependencies>
    </project>
    
That's it!  When I first read a pom, after years of reading Ant build scripts, I couldn't figure out what was supposed to happen.  It doesn't look like anything is going on - no compiling, no jarring, certainly no testing.


Again, as with the directory structure, Maven is implicit.  It has what Maven folks call a ["lifecycle."](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)


### Vocabulary Lesson


Ant people will benefit from a short vocabularly lesson to get up to speed with Maven jargon, and to get some googleable terms


* Lifecycle
    * The process for building and distributing an artifact
       * There are three lifecycles
           * default
               * Default builds and deploys your project.  Deploy might trip up those of you who are used to putting things on servers.  In this case, it does not mean 'deploy your webapp to Tomcat.'  Instead it means 'deploy the build artifact to a Maven repository'
           * clean
               * Clean cleans up your project, by deleting build products and intermediate clutter that the build creates.  In practice, this mostly means it deletes the `target` folder that Maven builds create
           * site
               * Site creates the documentation for your project's website.  Javadocs, junit test reports, findbugs reports and that sort of thing happen in the lifecycle
* Phase
    * Lifecycles are made of phases.  Maven keeps a [list of all the different phases in the Lifecycle Reference](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Lifecycle_Reference)
        * The most common phases a developer will interact are the phases composing the default lifecycle
            * validate
            * compile
            * test
            * package
            * verify
            * install
            * deploy
* Goal
    * Phases are made out of plugin goals.  If you read through a pom, you'll notice that `build` element, for example, often contains a number of plugins.  These plugins define what happens in a phase.
    * Goals can also be used independently of a lifecycle, to allow for a finer grained control over the build


### Using the Build Lifecycle


To use the build lifecycle, use the Maven command line and pass in any lifecycle, phase or goal name.


#### Examples


* Lifecycle
    * `mvn default`
* Phase
    * `mvn package`
* Goal
    * `mvn dependency:copy-dependecies`
    
You can pass multiple lifecycle arguments to maven and it will execute each of them in turn


Dependencies
=============


Dependencies is one of those places where I don't think there is a standard Ant way of dealing with them.  Ant people all know the labor of keeping the jars their project depends on in synce, and how hard it can be to distribute these jars to a team of developers.


I've seen a couple approaches in the Ant world.  Sometimes there is a folder on a shared network drive, and in the wiki for the project it tells devs to grab that folder and put it somewhere special relative to the project.  Other times, the jars are just included with the source code in the repository as big binary blobs.  Sometimes the jars get their own version control repo and devs are supposed to put the dependency repo in the same directory as their project repos, so all dependencies can be reached as `../dependency.jar`.  I've even seen a giant zip file with a pre-configured directory containing eclipse with all the projects set up and a directory of the repositories included in a known location, with a script for syncing the known location with a central server.


My point is, Ant doesn't really have a way of dealing with the problem with dependencies.  Regardless of what you are doing, you also have to manually compile the classpath and include that in your Ant file, which is another interesting excercise.


Where Maven shines, and what initially brings people to Maven, is its dependency management.  Maven will go get all your dependencies for you, build a classpath and can even make a fat jar for easy releases.  The only thing you need to get all the dependencies for a project is Maven, and a pom.


Maven also has the concept of "scopes" for dependencies.  Indicating that a dependency (like junit) is only required for the "test" scope will leave out that dependency when building the final artifact.


Basic Maven Usage
==================


Knowing how Maven is supposed to work is all well and good, but how do you actually use it?


In most cases, a developer probably wants to make a jar, war or ear that they can use or give to someone.


Here's how you do that from the command line:


`mvn package`


From Eclipse, right click on the project and select 'Run As' > 'Maven Build'.  The first time you do this, it will bring up the Run Configurations dialog.  Type 'package' into the goals field and run the build.


You might notice that these commands don't run the whole default lifecycle.  They skip the verify, install and deploy phases.  Those are a little more complicated than the basic differences between Maven and Ant that I try to illustrate here.  A separate article is probably required to talk about what installing and deploying mean in the Maven world, how they interact with IDEs and when they should be used.