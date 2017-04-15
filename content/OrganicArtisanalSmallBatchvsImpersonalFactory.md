﻿Title: Organic Artisanal Small Batch vs Impersonal Factory 
Slug: organic-artisanal-small-batch-vs-impersonal-factory
Modified: 2/4/2016 06:00
Date: 2/4/2016 06:00
Category: Programming
Tags: programming, culture, method, methodology, mindset, growth, style
Authors: Gunnar Gissel
Summary: Two styles of running a programming shop, their benefits and my preference


There are a couple approaches a shop can take to coding.  There is the "Organic, artisanal, small batch" programming and "Impersonal Factory" programming.


My transition from a small batch artisanal shop to an impersonal factory is recent.  The change is still fresh in my mind, while distant enough to have some perspective.  This is what the change from an artisanal shop to impersonal factory style coding is like:


Small shops and new devs take the organic route.  This is out of necessity.  You have to move fast, get code out the door and put food on the table and money in your pocket. 


Infrastructure is the other reason.  Small shops and new devs often have little infrastructure.  There may not be a build server and a staging server.  There may only be a laptop and production.


Organic, artisanal, small batch programming gets things done. If nobody sat down and banged out the first version of something we'd still be using slipsticks and filing cabinets.  Moreover, while teams are small and have low turnover, the cost to artisanal coding is minimal. If the author is there and can personally explain where the bodies are buried to a small group, style differences are barely a hiccup.


As shops grow, the merits of factory style programming becomes clear. I don't mean the [factory pattern.](https://en.wikipedia.org/wiki/Factory_\(object-oriented_programming\))  You [GOF people](https://en.wikipedia.org/wiki/Design_Patterns) can see yourselves out :)


At some point,  around 5 developers, the overhead from introducing new developers  begins to drag on the team's productivity. Different project formats and project that need leads to be responsible for building applications


The Solution
============


Stand up some shared infrastructure and standards.  Pairing shared infrastructure and standards together is absolutely necessary.  Without standards, shared infrastructure turns into a shared nightmare. Without shared infrastructure, you're left with standardized coding wizards mumbling into their own private grimoires.  No chance of telling whether or not the standards have been adopted.


The bare minimum for effective shared infrastructure is:


* A shared code repository


* A shared build server


* A place to put artifacts created by builds


* A staging server for testing deploys before they make it to production


What each of these elements mean is different depending on the stack your shop uses.  I'm in the boring enterprise world, so the stack I'm going to talk about is Oracle, Java and Javascript. 


Shared Code Repository
-----------------------


The specific tool your team uses doesn't matter, so long as it uses a tool and you are all storing code in the same place. According to [Zero Turnaround's 2016 tech survey](https://zeroturnaround.com/rebellabs/java-tools-and-technologies-landscape-2016/) Git (and presumably Github) is the clear winner for version contro, followed by Subversion. My shop uses Mercurial - we made the switch from CVS before it was clear that Git would win and haven't felt a strong need to switch just for the sake of switching.


I won't go into why you should use source control in 2017(!), but I want to emphasize that having a shared place where every developer gets and puts code is extremely valuable.


If you aren't using source control, get with the program.


Shared Build Server
---------------------


In 2017, developers should not be deploying artifacts to production that they create on their workstation. Partly this is because it can be difficult to recreate the state of a dev's workstation at a point in time well enough to recreate the artifact. Partly because manual processes like these have a poor [bus factor](https://en.wikipedia.org/wiki/Bus_factor) and are difficult to pass on to new devs.  Mostly because computer time is cheap, dev time is expensive, and automation is easy.


A build server provides a place to define the build and deploy process.  A place to record past builds.  A place to store artifacts.  One of the great benefits of a shared build server is that any developer can run a build by pressing a button.  It's a powerful advantage when a new hire can do a build on the first day they walk into the office.


Keeping deployed artifacts around another great benefit.  If you need to roll back, you can get the exact thing that was deployed last.  No manual copying out to a network file share, no wiki notes about where to find the backups.  Everything in one place!


Another benefit to a shared build server is that they can act like a friendly interface to `cron`.  Devs can easily script a repetitive task and then pass off the scheduling to Jenkins.  Jenkins keeps track of the scripts success and can email devs when there are problems.  It sounds small, but this is a huge productivity booster.


Artifact Repository
---------------------


A build server _can_ hold all your artifacts, up to a point.


Build servers are good at holding artifacts that get deployed to production servers.  Build servers are __not__ good at holding intermediate artifacts, like library jars. 


Jenkins can move jars between builds, but keeping track of which jar belongs to a build is difficult.  Like spaghetti code, spaghetti dependencies end in tears. 


Developers need access to intermediate artifacts, but build servers do not give easy access.  Sane Java development uses Maven, which can go get jars, but it needs to get them from a repository, not a build server.


Nexus is the artifact repository my shop uses.  It's an artifact repository that works with Maven and is self-hostable.  Thanks to Nexus, new projects can use existing libraries and tools without really trying.


Staging Server
-----------------


A staging server is a server where code is deployed before it is deployed to the production server.  The simplest way to use a staging server is as a simple smoke test - deploy your code, boot the server.  If it boots, A-OK.


A staging server can also be a test server.  Deploy code to the staging server, then run functional and user-acceptance tests. The staging environment is designed to be just like production.


If you aren't using a staging server, you're staging/testing in production, which is dangerous.


Reflections on the Change from Small Batch to Factory


=======================================================


The change from a small batch shop to a factory shop has been positive.  The speed of code development increased and the rate of recurrent bugs decreased.  The straightjacket of Maven, and the Nexus repository encourage modularity and code sharing, which allows us to build more complex systems quickly.


On the negative side, the speed of creating a new project with new infrastructure decreased.  More infrastructure for testing is required, which naturally increases the burden of rolling out new projects.


Increased automation has offset the infrastructure burden, but more automation remains to be done.


I wouldn't go back.