Title: Software Leadership Values
Slug: software-leadership-values
Date: 6/16/2017 20:45
Modified: 8/7/2017 20::00
Category: Meta
Tags:  meta, leadership, values
Authors: Gunnar Gissel
Summary: A clear conception of values is required to make judgement calls.  Here are 11 values that I believe are important for making good software


* Customers come first, but we must be kind to our future selves
* Supporting team members comes second
* Diversity of people, ideas and tools make better software
* People matter more than rules or being right
* Just because it isn't a bug, doesn't mean it isn't a problem
* Collaboration is far more powerful than lone-wolfing it
* Everyone should learn constantly and constantly share what they have learned
* We should maximize team happiness, but not spend a lot of time min-maxing
* We should use the best tool for each job
* Systems have greater power than tools and should be preferred
* Plan, but respond on your feet


Customers come first, but we must be kind to our future selves
------------------------------------------------------------------
Without customers, you wouldn't be working.  That makes them #1 - they are the reason you are here.  Customers are not always right, however.  They know what their problem is, but they may not know what the solution is.  You are the expert they are consulting.  Guide them to the best solution for them and for their problem.


My team had a customer with strong opinions on database implementation details.  She was a skilled queryer, and a business expert, but she was *not* a developer.  She usually wanted to know if a person in a database fit into a certain category.  Every time the request would be "can you add an 'in this category' flag to the database?".  Often the flags were really boolean checks that indicate whether a start or end date column is null.  Just blindly adding the flags adds one more thing to bookkeep in other processes and creates a substantial field for new and interesting errors.


Enabling her to do her job is our #1, but kindness to our future selves required that we understand her problem so we create a solution that doesn't impede solving future problems.  Rather than adding flags we gave her views and reports that appeared to have the desired flag, but used the existing data.


Supporting team members comes second
-------------------------------------


Supporting customers may be #1, but the team is #2.  Every member of the team should have every other member's back.  The team needs to get along to support the customers.


This is as simple as covering for someone when they are on leave, or swapping tasks to better balance workloads.  It also mean supporting your team members when something has gone wrong.  Never throw your team members under a bus or start a witch hunt - even if your customers are managers are demanding it.


Years ago, when I was a baby developer, my team had a powerful Ant script to tear down and rebuild the test database.  The script used two properties files to determine which database to point at.  In the course of normal development, I had pointed the script at production for some reason - maybe I was querying data, maybe I was fixing a problem live; I forget.  I changed gears and started in on some database development.  After writing my create statements, I burned down the database.  The production database.


Fortunately, the team was supportive.  They helped fix the immediate outage and gave me guidance on how to clean up the mess I had made in production.  No finger points, no blame, just a good lesson learned.  That is not the true test.  The true test is that I immediately did the same thing to our training application.  This was not ordinarily a production application, but a place to do demos for users.  I inadvertently destroyed it right before a big demo.


Even more fortunately, the team was _still_ supportive.  I applied the lessons I had just learned from the previous cleanup and had the training system up and running in time for the demo.  We used this series of mistakes as a learning experience, and removed the big red button from the day-to-day development controls.


Diversity of people, ideas and tools make better software
-----------------------------------------------------------
I don't know everything; nobody does.  People with the same background as I have generally know similar things to me.  People with different backgrounds know different things.  On a team this is great!  I can rely on my team members to make up for my shortcomings, and they can rely on me to make up their shortcomings.  The same is true for the collection of ideas and tools that make up your software.  


Mosaics make better art - each individual piece comprising a great whole.  [Chagall's _Four Seasons_](https://en.wikipedia.org/wiki/Four_Seasons_\(Chagall\)) is better than [Malevich's _Black Square_](https://en.wikipedia.org/wiki/Black_Square_\(painting\))


[McKinsey & Company](http://www.mckinsey.com/business-functions/organization/our-insights/why-diversity-matters) says a diverse company outperforms a non-diverse company by 35%!


Making sure applications work for everyone is a good thing - especially when they are required-by-law federal government applications.  Ensuring good accessibility is not quite hard, but there are a lot of moving pieces and things to consider.  I designed a series of icons to indicate statuses.  Two of them were a green and a red circle to indicate "Checked In" and "Checked Out".  A colorblind coworker pointed out that the icons were hard to distinguish for the color blind.  I incorporated my coworker's feedback and changed "Checked Out" to be a black square and added a tooltip to both, improving the accessibility of the application.


People matter more than rules or being right
-----------------------------------------------


The people that you work with, and the people that you serve matter more than strict adherence to rules and the desire to be 'right'.  The relationships between team members, customers and users are an invisible system that creates a business and software.  Damaging these relationships for the sake of adherence to minor rules or technical rightness does a large amount of harm that echoes through the future.


This isn't to say that all rules can be broken for the sake of relationships; an effort must be made to distinguish between rules that are 'bright lines' never to be crossed and rules that are 'broccoli' a good idea most of the time, but not all the time.  The recognition that rules are human creations and are meant to serve us, not the other way around, is key.


At my work, there is a rule that logbooks are indelible - written in ink.  They are supposed to be a record of what a boat is doing, as the boat does it.  Sometimes, through software or peopleware faults, mistakes are made.  Maybe the boat records what it is doing, but in the wrong month.  It's 'against the rules' to delete their entries, but the intent of the rules is to ensure a high level of data quality.  Preserving garbage data to comply with rules runs contrary to the intent of the rule, so I violate this rule when needed (after due consultation with stakeholders and affected parties).


Other rules are so fundamental that they can never be violated.  I handle a lot of 'confidential business information' for a variety of businesses.  There are no circumstances where I would ever disclose this information to someone who was not already working for NOAA on this information.  Not even to the business that generated the info - they should already know it!


Just because it isn't a bug, doesn't mean it isn't a problem
--------------------------------------------------------------


Part of every developer's job should involve a certain amount of user support.  Not too much; that's a waste of expensive time, but enough to ensure developers keep their ear to the ground and hear what people are really saying.  It's common that most problems aren't really software bugs - the system is working as designed.  If users keep running into the same problem, developers should try to understand _why_ they are having the problem and what they can do to help.  Often, altering workflow, behavior or presentation a small amount will cause 'not a bug' support issues to evaporate.


A project I worked on supported a government-required annual process.  Every year, at the start of the process, the help desk was overwhelmed with phone calls about how to begin the process.  The help desk was very small, so I assisted users when the help desk was busy.  As I worked with users, I noticed a trend:


The program, as designed, only allowed users to choose valid options.  Any button the user pushed would work and be an ok choice.  This was not enough - users lacked confidence to choose which button to push on their own.  


After the second year of support validated that the problem was not just users having trouble with a brand new program, I sat and thought about what was happening.  I realized that users needed a little confidence boost to get started.  I created a wizard with that guided users through the stakeholder's preferred workflow.  The next year, support calls about getting started dropped to zero.  


Collaboration is far more powerful than lone-wolfing it
--------------------------------------------------------------


"Everybody knows" that collaboration is good and has powerful results.  It is very easy for developers to become absorbed in the problem at hand and to forgo collaboration.


Everyone should learn constantly and constantly share what they have learned
---------------------------------------------------------------------------------


Programmers must learn constantly as a primary function of their job.  Programming is the discipline of creating tools to solve unsolved problems; if the problem was solved people would just buy the off the shelf solution.  Solving unsolved problems requires some amount of learning.


The key to building an organization that effectively uses programming is to ensure programmers do not lock this knowledge up in their skulls.  They _need_ to share, and not only that, developers typically _like_ to share.


I've been fortunate on my development path; the organizations I've worked for are very supportive of training and resources for learning and growth.  When I started at NOAA, developers could go to two out of town conferences/year with the condition that they presented what they learned when they got back.  We've since expanded to a standing hour slot on Thursdays for demoing tech-things that we've learned.  Our goal is to make sharing learning so normal that it is boring.


We should maximize team happiness, but not spend a lot of time min-maxing
---------------------------------------------------------------------------


Decision points where two options are roughly equal should go to the option that increases team happiness.  It is more important that a decision is made, however, than the absolute 'best' decision is made.  Teams and their morale suffer when too much time is spent dithering over options.


Part of leadership is noticing when a team can't make up its own mind and deciding for them.  It may be that the decision is not an imperial, "Thou shalt do option A and only option A", but a diplomatic, "We've carefully evaluated options A and B.  They are both strong contenders, but based on blah, we are going to use option A for the time being".  Teams are happier when they feel like they have clear direction and guidance.


I've worked much of my career in positions that are in between supervisors.  My supervisors have quit, transferred, been promoted and died.  Whatever the reason, acting supervisors aren't typically able to fill the role of a full time permanent supervisor because they know they'll be returning to their old relationship to the team in a short while.  The upshot is that I've spent a lot of time engaging in collaborative decision making with team members.


We have a solid team, and usually we can come to a consensus decision, or at least a consensus decision process without any trouble.  The times when we have had a unresolvable disagreement have been amicable, but without a designated leader to break the tie they bog us down.  A leader who can move the team past these knots of disagreement is valuable.


We should use the best tool for each job
--------------------------------------------


Developers within an organization must be empowered to use the best tool for the job at hand.  They must not be constrained to use only the organization's current tool set.


Systems have greater power than tools and should be preferred
--------------------------------------------------------------


Software developers love tools, or at least they use a lot of tools.  Tools require upkeep and developer intervention.  Systems, in particular automated systems, require less upkeep and direct developer intervention.  Systems are generally composed of multiple tools.  The more systems that developers create, the more developers multiply their own force.  Tool-based systems that require developers to keep on top of all their tools and usages divide developer's force.






Plan, but respond on your feet
----------------------------------


Planning is key to pulling off projects with success.  Plans, designs, milestones and so on should be made, but they must be malleable.  A rigid plan is not resilient - the plan must be able to accommodate changing facts and premises.