Title: Turn Your Spaghetti Code into Functions - Part 1
Slug: turn-your-spaghetti-code-into-functions-part-1
Date: 08/07/2017 19:15
Modified: 08/07/2017 19:15
Category: Programming
Tags: java, technique, diy, how-to, tutorial, guide, lambda, function, refactor
Authors: Gunnar Gissel
Summary: Don't fight with your code, let your code fight for you.  Use clever refactoring and clearly named functions to get easy, re-usable, extensible business rules.




<img src="i.imgur.com/WtnFFKs.png" title="Cramming an elephant into a Smart Car" />


Developers can sink a lot of hours into fighting business rule code.  [Spaghetti business rules](https://en.wikipedia.org/wiki/Spaghetti_code) make it so little changes need to be copy pasted repeatedly throughout if/else blocks.  It's like trying to shoehorn an elephant into a Smart Car, when it should be like snapping together legos.


Anyone who has worked on a 'mature' set of business rules knows that untangling what is going on is extremely hard.  If cramming the elephant into the Smart Car was tough, getting it out is an order of magnitude tougher.  I'm going to show how to make your Smart Car-driving elephant a little happier.


Business rules are your money-makers and form the essence of your business's being.  They also change _a lot._  This dynamic often leads to rushed work in business rules and over the long run creates a nasty mess right in the heart of your money maker.  A nasty mess is hard to read and even harder to figure out what it is supposed to be doing.  


Further, the OO way of encapsulating business rules is either fundamentally inadequate, or so widely misunderstood by working developers that the common pattern is a [god class](https://en.wikipedia.org/wiki/God_object) that mutates everything it touches.  Testing a huge class, stuffed with spaghetti and mutators is daunting, at best, impossible at worst.  No tests make it very hard to develop without fear.


Here's a set of techniques for making the code easier to follow, so you can put your effort into understanding your stakeholders and making sure what's in the code is what they _want_ to be in the code.


This will teach you how to untangle business rules, so you can easily work with them.


### Readability

<img src="i.imgur.com/yU7tDJnm.jpg" title="Books!" />

Deep nesting impairs readability.  Even when developers use tabs well and are consistent with their curly brace usage, around the 3rd layer of if/else statements, it starts getting hard to tell what particular branch you are reading.


> Is this the one with the null child object?  I'll just check for null again here really quick


Avoid this kind of impulse by structuring your code so there is never any doubt about what you are checking.


Long conditions that reach deep into child or grandchild objects also impair readability.  Stakeholders never say (unless they've been terribly abused) something like:


> If the transfer type code is 200 and it's not in areas 907, 412 or 213, then it's not allowed


1. That's got more "nots" than a human likes to say
2. Humans don't usually go on about codes.  


They might say something like:


> If it's a partner transaction, we only allow it in partner areas


If your code takes mental backflips to match how your stakeholders talk, you're gonna have a bad time.  So are they, and they won't even know why.


### Testability


Gnarly business rule code is hard to test.  The twists and turns of deeply nested if/else statements are easy to get lost in, easy to forget a branch and sometimes just plain impossible to set up in a testing harness.  No tests mean every change is dangerous - you are one misplaced `}`, or backwards `>` from giving your users a headache.

<img src="i.imgur.com/UEHFn8Am.jpg" title="Mutant strawberry" />

Gnarly business rule code seems to encourage devs to mutate the objects it is validating.  I don't know why this is, but I've seen it many times in the wild.  State mutation amps up the testing difficulty by an order of magnitude.  Now, not only must you test for messages and expected errors, but you must detect changes to the object you are validating.  Are they intentional?  Are they correct?


Who knows?  I promise no one wrote it down.

### Response speed


Stakeholders, users, managers and developers constantly engage in timeline tug of war.  Technical debt hamstrings developers' ability to give their users what they need.  A good 'tell' that your system has a lot of technical debt is users can easily describe a feature, but developers can't easily implement it.  The simplest things turn into month long bushwhacking exercises.


<img src="i.imgur.com/PCMKeOMm.jpg" title="Devil's Club is thorny" />


To me, nothing says bushwhacking like coming down a mountain, getting off trail and fighting through [Devil's Club](https://en.wikipedia.org/wiki/Devil%27s_club) and loose scree - 


Wait.  I meant nothing says bushwhacking like coming into a method and getting on the wrong nested if/else branch and fixing something that wasn't broken in the first place.  Or noticing that 100 lines of code have never, ever been executed, because they wouldn't work.  Or any number of the fun surprises that spaghetti-fied business rules bring.


### Composability


Composability lets you create new rules out of old rules.  Most new business rules have a lot in common with existing rules.  The ability to combine existing rules and add that _one special case_ is extremely powerful.  Your stakeholders will be amazed at your turnaround time!


The spaghetti style is anti-composable.  Copy-pasting, duplicating code and mangling switch statements are practically requirements with spaghetti-ed business rules.  Good luck re-using something to get at the one 


Example Bad Code
-----------------------------


[Here's an example of standard Java business logic](https://github.com/monknomo/If-Else-Block-Refactoring/tree/master/src/main/java/com/gunnargissel/suemez/businessrulerefactorexample) that evaluates a business object (`BusinessTransfer`) and creates messages to return to the user if it violates business rules:


    public static final String checkWidgetTransfer(WidgetTransfer transfer) {
        String businessRuleErrors = "";

        if (transfer.getTransferer().getAccount(transfer.getFromAccount()).getBalance().compareTo(transfer.getAmount()) < 0) {
            businessRuleErrors += "Insufficient balance to transfer ; ";
        }


        if (transfer.getTransferTypeCode().equals("200")) {
            if (!transfer.getAreaCode().matches("907|412|213")) {
                businessRuleErrors += "This area is not a transfer eligible area. ; ";
            } else if (!transfer.getAreaCode().matches("213")) {
                if (transfer.getTransferer().getCategory().equals("D")) {
                    businessRuleErrors += "D Category Transferer can only be transferred in transfer area 213. ; ";
                }
            }
        } else if (transfer.getTransferTypeCode().equals("710")) {
            if (!transfer.getAreaCode().matches("574|213|363|510")) {
                businessRuleErrors += "This area is not a transfer eligible area. ; ";
            }
        }


        if (transfer.getTypeCode().equals("I")) {
            if (isBlockSize(transfer)) {
                businessRuleErrors += "Amount is too small for I type transfer. ; ";
            }
            if (isTotalOverCap(transfer)) {
                businessRuleErrors += "This transfer is too large. ; ";
            }
        }
        
        return businessRuleErrors;
    }


    public static boolean isBlockSize(WidgetTransfer transfer) {
        return transfer.getAmount().compareTo(1000) < 0;
    }


    public static boolean isTotalOverCap(WidgetTransfer transfer) {
        return transfer.getAmount().compareTo(1000000) > 0;
    }
    
The above example is inspired by actual code running in the wild.  What I show here is simplified, and anonymized.  It's as hard to read as the original.  


Reading it takes knowledge of what a "200" transfer type code is or what is acceptable data for different transfer area codes.  The parentheses are nested, which makes copy-pasting (a common technique for working with this style of code) perilous.  A dev can't afford to miss a single curly bracket without causing a hard-to-debug problem.
    
Logic Block Paradigm Shift
---------------------------


[A quick way of refactoring long branching `if/else` code is to dispense with branches and with `elses`.](https://github.com/monknomo/If-Else-Block-Refactoring/tree/master/src/main/java/com/gunnargissel/suemez/businessrulerefactorexample/refactor1)  By rephrasing each business rule into a positive constraint, a developer can check to see if the constraint conditions are met, rather than walking a branching logic tree.  This technique increases line count a little, but improves readability a lot.


Another low hanging fruit is to create instance variables to hold values, rather than use getters (or worse, nested getters!).  This gives the ability to name what a thing is in the context you are using it in, rather than relying on getters to have a good name in your context.


    public static final String checkWidgetTransfer(WidgetTransfer transfer ) {
        String businessRuleErrors = "";
        Integer balance = transfer.getTransferer().getAccount(transfer.getFromAccount()).getBalance();
        Integer transferAmount = transfer.getAmount();
        String transferTypeCode = transfer.getTransferTypeCode();
        String areaCode = transfer.getAreaCode();
        String category = transfer.getTransferer().getCategory();
        String typeCode = transfer.getTypeCode();


        if (balance.compareTo(transferAmount) > 0) {
            businessRuleErrors += "Insufficient balance to transfer ; ";
        }


        {
            if (transferTypeCode.equals("200")
                    && !areaCode.matches("907|412|213")) {
                businessRuleErrors += "This area is not a transfer eligible area. ; ";
            }
        }


        if (transferTypeCode.equals("200")
                && areaCode.matches("213")
                && category.equals("D")) {
            businessRuleErrors += "D Category Transferer can only be transferred in transfer area 213. ; ";
        }


        if (transferTypeCode.equals("710")
                && !areaCode.matches("574|213|363|510")) {
            businessRuleErrors += "This area is not an eligible area. ; ";


        }


        if (!typeCode.equals("I")
                && !isBlockSize(transfer)) {
            businessRuleErrors += "Amount is too small for I type transfer. ; ";
        }


        if (!typeCode.equals("I")
                && isTotalOverCap(transfer)) {
            businessRuleErrors += "This transfer is too large. ; ";
        }

        return businessRuleErrors;
    }
    
### The Good


* The above code is much more readable.  
    * Each business rule is contained in its own block of logic
    * All the properties needed to determine whether a condition has been met are named.  
    * You can describe each business rule as written and it very nearly sounds like English.
* The logic blocks are small and discrete.  
    * There are no nested curly braces, so you'll have a hard time getting lost in the code.


### The Bad


* Business knowledge of what codes mean is still required
    * What is a "200" transfer type code?  The code doesn't say, so hopefully it is documented somewhere...
* Negative conditionals abound - `if (!typeCode.equals("I"))`
    * Negative conditionals are a little hard to say, and are harder to reason with than positive conditionals.
* Still mutating those `businessErrorMessages`
    * This is just one more thing to set up in a unit test


## What's Next?


I'll continue this refactoring discussion in a couple future posts.  Check out my [example refactoring repository](https://github.com/monknomo/If-Else-Block-Refactoring) for a preview!


We're going to see:


* How to use Predicates to make your life better
* Using actual objects, and not just their properties, to make your life better
* Using Functions and validator objects, to make your life better


We'll try to get that elephant in his Smart Car, but mostly we'll try to make your life better.


<img src="https://i.imgur.com/xfmb1Bs.png"  title="An elephant driving a Smart Car"/>


## Credits


_Thank you [Volantra](https://www.flickr.com/photos/volantra/) for the [right facing Smart Car Pic](https://flic.kr/p/74L2vC)_


_Thank you [roebot](https://www.flickr.com/photos/roebot/) for the [left facing Smart Car](https://flic.kr/p/73uXD3)_


_Thank you [Oliver Dodd](https://www.flickr.com/photos/oliverdodd/) for the [elephant](https://flic.kr/p/8N681r)_


_Thank you [Neils Heidenreich](https://www.flickr.com/photos/schoschie/) for the [mutant strawberry](https://flic.kr/p/4VX3xT)_


_Thank you [Peter Stevens](https://www.flickr.com/photos/nordique/) for the [Devil's Club](https://flic.kr/p/zfoSkn)_

_Thank you to [Erica Schoonmaker](https://www.flickr.com/photos/_erica/) for the picture of the [books](https://flic.kr/p/9EUVrx)_