Title: Software Leadership Values
Slug: software-leadership-values
Date: 6/16/2017 20:45
Modified: 8/10/2017 20:00
Category: Meta
Tags:  meta, leadership, values, about
Authors: Gunnar Gissel
Summary: A clear conception of values is required to make judgement calls.  Here are 11 values that I believe are important for making good software


<a id="top">Software Leadership Values</a>
========================


It's important to know what your values are, so as you make decisions, you have a set of broad principles to fallback on when making judgement calls.  Public accountability is also very useful in encouraging people to adhere to their values.


I've written down 11 values that I think are important for making good software, and am publishing them so I have a reference to look back at and so others both know where I'm coming from and can tell me if I'm not even following my own espoused values.


* [Customers come first, but we must be kind to our future selves](#customerFirst)
* [Supporting team members comes second](#supportTeam)
* [Diversity of people, ideas and tools make better software](#diversity)
* [People matter more than rules or being right](#peopleMatter)
* [Just because it isn't a bug, doesn't mean it isn't a problem](#nonBugProblems)
* [Collaboration is far more powerful than lone-wolfing it](#collaboration)
* [Everyone should learn constantly and constantly share what they have learned](#constantLearning)
* [We should maximize team happiness, but not spend a lot of time min-maxing](#maximizeHappiness)
* [We should use the best tool for each job](#bestTools)
* [Systems have greater power than tools and should be preferred](#preferSystems)
* [Plan, but respond on your feet](#planResponsively)




<a id="customerFirst"></a>Customers come first, but we must be kind to our future selves
------------------------------------------------------------------


[Back to list](#top)


Without customers, you wouldn't be working.  That makes them #1 - they are the reason you are here.  Customers are not always right, however.  They know what their problem is, but they may not know what the solution is.  You are the expert they are consulting.  Guide them to the best solution for them and for their problem.


My team had a customer with strong opinions on database implementation details.  She was a skilled queryer, and a business expert, but she was *not* a developer.  She usually wanted to know if a person in a database fit into a certain category.  Every time the request would be "can you add an 'in this category' flag to the database?".  Often the flags were really boolean checks that indicate whether a start or end date column is null.  Just blindly adding the flags adds one more thing to bookkeep in other processes and creates a substantial field for new and interesting errors.


Enabling her to do her job is our #1, but kindness to our future selves required that we understand her problem so we create a solution that doesn't impede solving future problems.  Rather than adding flags we gave her views and reports that appeared to have the desired flag, but used the existing data.


<a id="supportTeam"></a>Supporting team members comes second
-------------------------------------


[Back to list](#top)


Supporting customers may be #1, but the team is #2.  Every member of the team should have every other member's back.  The team needs to get along to support the customers.


This is as simple as covering for someone when they are on leave, or swapping tasks to better balance workloads.  It also mean supporting your team members when something has gone wrong.  Never throw your team members under a bus or start a witch hunt - even if your customers are managers are demanding it.


Years ago, when I was a baby developer, my team had a powerful Ant script to tear down and rebuild the test database.  The script used two properties files to determine which database to point at.  In the course of normal development, I had pointed the script at production for some reason - maybe I was querying data, maybe I was fixing a problem live; I forget.  I changed gears and started in on some database development.  After writing my create statements, I burned down the database.  The production database.


Fortunately, the team was supportive.  They helped fix the immediate outage and gave me guidance on how to clean up the mess I had made in production.  No finger points, no blame, just a good lesson learned.  That is not the true test.  The true test is that I immediately did the same thing to our training application.  This was not ordinarily a production application, but a place to do demos for users.  I inadvertently destroyed it right before a big demo.


Even more fortunately, the team was _still_ supportive.  I applied the lessons I had just learned from the previous cleanup and had the training system up and running in time for the demo.  We used this series of mistakes as a learning experience, and removed the big red button from the day-to-day development controls.


<a id="diversity"></a>Diversity of people, ideas and tools make better software
-----------------------------------------------------------


[Back to list](#top)


I don't know everything; nobody does.  People with the same background as I have generally know similar things to me.  People with different backgrounds know different things.  On a team this is great!  I can rely on my team members to make up for my shortcomings, and they can rely on me to make up their shortcomings.  The same is true for the collection of ideas and tools that make up your software.  


Mosaics make better art - each individual piece comprising a great whole.  [Chagall's _Four Seasons_](https://en.wikipedia.org/wiki/Four_Seasons_\(Chagall\)) is better than [Malevich's _Black Square_](https://en.wikipedia.org/wiki/Black_Square_\(painting\))


[McKinsey & Company](https://www.mckinsey.com/business-functions/organization/our-insights/why-diversity-matters) says a diverse company outperforms a non-diverse company by 35%!


Making sure applications work for everyone is a good thing - especially when they are required-by-law federal government applications.  Ensuring good accessibility is not quite hard, but there are a lot of moving pieces and things to consider.  I designed a series of icons to indicate statuses.  Two of them were a green and a red circle to indicate "Checked In" and "Checked Out".  A colorblind coworker pointed out that the icons were hard to distinguish for the color blind.  I incorporated my coworker's feedback and changed "Checked Out" to be a black square and added a tooltip to both, improving the accessibility of the application.


<a id="peopleMatter"></a>People matter more than rules or being right
-----------------------------------------------


[Back to list](#top)


The people that you work with, and the people that you serve matter more than strict adherence to rules and the desire to be 'right'.  The relationships between team members, customers and users are an invisible system that creates a business and software.  Damaging these relationships for the sake of adherence to minor rules or technical rightness does a large amount of harm that echoes through the future.


This isn't to say that all rules can be broken for the sake of relationships; an effort must be made to distinguish between rules that are 'bright lines' never to be crossed and rules that are 'broccoli' a good idea most of the time, but not all the time.  The recognition that rules are human creations and are meant to serve us, not the other way around, is key.


At my work, there is a rule that logbooks are indelible - written in ink.  They are supposed to be a record of what a boat is doing, as the boat does it.  Sometimes, through software or peopleware faults, mistakes are made.  Maybe the boat records what it is doing, but in the wrong month.  It's 'against the rules' to delete their entries, but the intent of the rules is to ensure a high level of data quality.  Preserving garbage data to comply with rules runs contrary to the intent of the rule, so I violate this rule when needed (after due consultation with stakeholders and affected parties).


Other rules are so fundamental that they can never be violated.  I handle a lot of 'confidential business information' for a variety of businesses.  There are no circumstances where I would ever disclose this information to someone who was not already working for NOAA on this information.  Not even to the business that generated the info - they should already know it!


<a id="nonBugProblems"></a>Just because it isn't a bug, doesn't mean it isn't a problem
--------------------------------------------------------------


[Back to list](#top)


Part of every developer's job should involve a certain amount of user support.  Not too much; that's a waste of expensive time, but enough to ensure developers keep their ear to the ground and hear what people are really saying.  It's common that most problems aren't really software bugs - the system is working as designed.  If users keep running into the same problem, developers should try to understand _why_ they are having the problem and what they can do to help.  Often, altering workflow, behavior or presentation a small amount will cause 'not a bug' support issues to evaporate.


A project I worked on supported a government-required annual process.  Every year, at the start of the process, the help desk was overwhelmed with phone calls about how to begin the process.  The help desk was very small, so I assisted users when the help desk was busy.  As I worked with users, I noticed a trend:


The program, as designed, only allowed users to choose valid options.  Any button the user pushed would work and be an ok choice.  This was not enough - users lacked confidence to choose which button to push on their own.  


After the second year of support validated that the problem was not just users having trouble with a brand new program, I sat and thought about what was happening.  I realized that users needed a little confidence boost to get started.  I created a wizard with that guided users through the stakeholder's preferred workflow.  The next year, support calls about getting started dropped to zero.  


<a id="collaboration"></a>Collaboration is far more powerful than lone-wolfing it
--------------------------------------------------------------


"Everybody knows" that collaboration is good and has powerful results.  It is very easy for developers to become absorbed in the problem at hand and to forgo collaboration.


I can't count the number of times where working with other people, and sharing ideas, techniques and opinions has created something much better than either one of would have made alone.  Sometimes collaborating feels slower, because communication has a certain amount of overhead, and collaborating with even a small team takes an absurd amount of meeting, pairing, phone calls, emails and chats.  I think it is all worth it, because when things start being delivered they are a) better overall and b) understood by more than one person.


I view collaboration as not only a way to fill in my blindspots and shortcomings, but as savings on training, maintenance and emergency response.  When I am the sole developer, I am generally the only person who knows how what I've developed works.  That means I'm on the hook for all future features, all maintenance and it's my phone that rings when something goes wrong.  Collaborating spreads the knowledge and the workload around _automatically._


<a id="constantLearning"></a>Everyone should learn constantly and constantly share what they have learned
---------------------------------------------------------------------------------


[Back to list](#top)


Programmers must learn constantly as a primary function of their job.  Programming is the discipline of creating tools to solve unsolved problems; if the problem was solved people would just buy the off the shelf solution.  Solving unsolved problems requires some amount of learning.


The key to building an organization that effectively uses programming is to ensure programmers do not lock this knowledge up in their skulls.  They _need_ to share, and not only that, developers typically _like_ to share.


I've been fortunate on my development path; the organizations I've worked for are very supportive of training and resources for learning and growth.  When I started at NOAA, developers could go to two out of town conferences/year with the condition that they presented what they learned when they got back.  We've since expanded to a standing hour slot on Thursdays for demoing tech-things that we've learned.  Our goal is to make sharing learning so normal that it is boring.


<a id="maximizeHappiness"></a>We should maximize team happiness, but not spend a lot of time min-maxing
---------------------------------------------------------------------------


[Back to list](#top)


Decision points where two options are roughly equal should go to the option that increases team happiness.  It is more important that a decision is made, however, than the absolute 'best' decision is made.  Teams and their morale suffer when too much time is spent dithering over options.


Part of leadership is noticing when a team can't make up its own mind and deciding for them.  It may be that the decision is not an imperial, "Thou shalt do option A and only option A", but a diplomatic, "We've carefully evaluated options A and B.  They are both strong contenders, but based on blah, we are going to use option A for the time being".  Teams are happier when they feel like they have clear direction and guidance.


I've worked much of my career in positions that are in between supervisors.  My supervisors have quit, transferred, been promoted and died.  Whatever the reason, acting supervisors aren't typically able to fill the role of a full time permanent supervisor because they know they'll be returning to their old relationship to the team in a short while.  The upshot is that I've spent a lot of time engaging in collaborative decision making with team members.


We have a solid team, and usually we can come to a consensus decision, or at least a consensus decision process without any trouble.  The times when we have had a unresolvable disagreement have been amicable, but without a designated leader to break the tie they bog us down.  A leader who can move the team past these knots of disagreement is valuable.


<a id="bestTools"></a>We should use the best tool for each job
--------------------------------------------


[Back to list](#top)


Developers within an organization must be empowered to use the best tool for the job at hand.  They must not be constrained to use only the organization's current tool set.  Even so, "best" should include an honest evaluation of whether or not the tool is suited to the team.  If Go has the best tool, but your team is all Javascript programmers, you might want to go to "best tool that Javascript programmers can use".


I work with a team that does lots of Java and lots of PL/SQL.  We mostly make webapps, so our products are principally ears and wars.  In the not-so-distant past, the tools we used to make our ears and wars were Ant and Eclipse.  We kept zip files of our dependencies on a shared network drive and extensive wiki pages about how to set up and configure our development environments.


After a certain point, it because really obvious that changing dependencies, and bringing on new developers were our big pains.  We started down the road of putting zip files in source control, and scripting pulling and versioning our dependency zip files when a lightbulb turned on:


__We could change our tooling__


We switched to Maven and started running an internal Nexus server and never looked back.  It was a fair sized mountain to climb, but realizing that we should use tools that help and enable us to work without fighting tooling was a game-changing revelation.


<a id="preferSystems"></a>Systems have greater power than tools and should be preferred
--------------------------------------------------------------


[Back to list](#top)


I know I just said that using the best tool for the job is one of my core software leadership values.  Here's the flipside


Software developers love tools, or at least they use a lot of tools.  But!  Tools require upkeep and developer intervention.  


Systems, in particular automated systems, require less upkeep and less direct developer intervention.  Systems are generally composed of multiple tools.  The more systems that developers create, the more developers multiply their own, and their team's, force.  


Tool-based workflows that lack a system that require developers to keep on top of all their tools and usages divide developer's force.  The problem is compounded when working with a team is factored in.  Seemingly minor differences in how team members use tools can create strange problems, and the overhead involved in keeping all team member's tool usage in sync is _considerable._


At NOAA, I work on two different projects.  One depends on Maven, Jenkins and a continuous integration + a frequent (though not yet continuous) deployment process.  The other depends on Ant, a bunch of bash scripts, [Druid](https://sourceforge.net/projects/druid/?source=directory), dbUnit, really more than I care to list.


The first project has nicely documented procedures, the most common of which amount to "push a button, watch the result, respond in these ways".  The second project has many, many procedures for what order to use each tool and what directory to put each tool in, and where build products must be copied, and so on and so forth.


The first project is not only more productive, but it is more pleasant to work in and has been actively cannibalizing developers from the second project.  All thanks to some systems that allow developers to develop, instead of copy-paste procedures from wikis into a multitude of tools and argue over the phone about who missed a step in the wiki.


<a id="planResponsively"></a>Plan, but respond on your feet
----------------------------------


[Back to list](#top)


Planning is key to pulling off projects with success.  Plans, designs, milestones and so on should be made, but they must be malleable.  A rigid plan is not resilient - the plan must be able to accommodate changing facts and premises.


I have been lucky in my career.  My stakeholders have always recognized that elasticity must be baked into a plan.  Not only can schedules slip, but feature needs can change or emergent situations can arise.


Not infrequently, we develop systems to implement regulations that don't exist yet.  Depending on the regulatory side of the house, we may have implemented a system that doesn't match the final version of the regulations or the regulations are never formally adopted, so the system is put aside.  Leading a moving target, like unfinalized regulations, requires a plan that incorporates key decision points that are triggered by external events.  Certain events trigger questions like "Do we keep going?" or "What can we drop to hit the effective date?"


Building plans with this kind of flexibility is a great relief to both developers and stakeholders.


Credits
---------
_Thank you [Mark Freeth](https://www.flickr.com/photos/freetheimage/) for the [robin!](https://flic.kr/p/rR2UWM)_