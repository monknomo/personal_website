Title: Turn Your Spaghetti Code into Functions - Part 3
Slug: turn-your-spaghetti-code-into-functions-part-3
Date: 3/19/2018 20:07
Modified: 3/19/2018 20:07
Category: Programming
Tags: java, technique, diy, how-to, tutorial, guide, lambda, function, refactor
Authors: Gunnar Gissel
Summary: How the validator pattern makes business rules easy to test, transport and package

Start with [Part 1](https://www.gunnargissel.com/turn-your-spaghetti-code-into-functions-part-1.html) and [Part 2](https://www.gunnargissel.com/turn-your-spaghetti-code-into-functions-part-2.html) first.

Picking up [where we left off in Part II]( https://www.gunnargissel.com/turn-your-spaghetti-code-into-functions-part-2.html ), let's set the stage for using a validator.   We left our example elephant in a cool convertible, but let's upgrade his ride to a rocket ship.  We'll start like all good rocket scientists - with a round of cleaning!

<img src="https://i.imgur.com/HS1ZVqFl.png" title="elephant driving a space shuttle" alt="elephant driving a space shuttle" />

After _[mise en place](https://en.wikipedia.org/wiki/Mise_en_place)_, we will be ready to implement a `Validator` and `Result`, which will create a single, standard, expandable format for business rules and an api for consuming results from business rule queries.  No more guessing what a rule-compliant call looks like!  No more stringing together crystal towers of nested boolean logic!

Cleanup
-----------

 There are a couple places where we used `.and()` to combine predicates in an `if` block.  Replace those with an independent predicate, so all `if` blocks refer to only one predicate

    static final Predicate<WidgetTransfer> suffientAmount = trans -> trans.getTransferer().getAccount(trans.getFromAccount()).getBalance().compareTo(trans.getAmount()) < 0;
        static final Predicate<WidgetTransfer> isPartner = trans -> trans.getTransferTypeCode().equals("200");
        static final Predicate<WidgetTransfer> isFriendsAndFamily = trans -> trans.getTransferTypeCode().equals("710");
        static final Predicate<WidgetTransfer> isFriendAndFamilyDiscountLegal = trans -> trans.getAreaCode().matches("574|213|363|510");
        static final Predicate<WidgetTransfer> isPartneringArea = trans -> trans.getAreaCode().matches("907|412|213");
        static final Predicate<WidgetTransfer> isDirigibleForbiddenArea = trans -> trans.getAreaCode().matches("213");
        static final Predicate<WidgetTransfer> isDirigibleCategory = trans -> trans.getTransferer().getCategory().equals("D");
        static final Predicate<WidgetTransfer> isInternal = trans -> trans.getTypeCode().equals("I");
        static final Predicate<WidgetTransfer> isBlockSize = trans -> isBlockSize(trans);
        static final Predicate<WidgetTransfer> isTotalOverCap = trans -> isTotalOverCap(trans);
        
        static final Predicate<WidgetTransfer> parterTransferReqs = trans -> isPartner.and(isPartneringArea.negate()).test(trans);
        static final Predicate<WidgetTransfer> dirigibleTransferReqs = trans -> isPartner.and(isDirigibleForbiddenArea.negate()).and(isDirigibleCategory).test(trans);
        static final Predicate<WidgetTransfer> friendsAndFamilyReqs = trans -> isFriendsAndFamily.and(isFriendAndFamilyDiscountLegal.negate()).test(trans);
        static final Predicate<WidgetTransfer> internalBlockReqs = trans -> isInternal.and(isBlockSize).test(trans);
        static final Predicate<WidgetTransfer> internalTotalCapReqs = trans -> isInternal.and(isTotalOverCap).test(trans);
        
        public static final String checkWidgetTransfer(WidgetTransfer transfer) {
            String businessRuleErrors = "";

            if (suffientAmount.test(transfer)) {
                businessRuleErrors += "Insufficient balance to transfer ; ";
            }

            if (parterTransferReqs.test(transfer)) {
                businessRuleErrors += "This area is not a transfer eligible area. ; ";
            }

            if (dirigibleTransferReqs.test(transfer)) {
                businessRuleErrors += "D Category Transferer can only be transferred in transfer area 213. ; ";
            }

            if (friendsAndFamilyReqs.test(transfer)) {
                businessRuleErrors += "This area is not a transfer eligible area. ; ";
            }

            if (internalBlockReqs.test(transfer)) {
                businessRuleErrors += "Amount is too small for I type transfer. ; ";
            }

            if (internalTotalCapReqs.test(transfer)) {
                businessRuleErrors += "This transfer is too large. ; ";
            }

            return businessRuleErrors;
        }
        

The above code has a lot of boiler plate - but it's boiler plate that is invisible to the average Java dev.  All those `if` blocks are boiler plate.  You have to type them again, and again.  What if I told you, you could use a validator and clean up all your business rules?  Think of the miles of conditionals in your business code, and imagine each reduced to a single composable function call.

Boilerplate Removal
-------------------------------------------

<img src="https://i.imgur.com/z5pXylbl.jpg" title="literal boiler plate"/>

Another problem is that `checkWidgetTransfer` returns a string.  This pushes the responsibility for determining if an error has occured onto the calling method.  All `checkWidgetTransfer` callers need a section that looks like this:
    
    String result = checkWidgetTransfer(transfer);
    if(null == result || 0 == result.size()) {
        //continue
    }else{
        handleError(result);
    }

Multiply this by every bizarre process that Bob in accounting, Carol in sales uses and Duane in HQ uses.  It can get.... __big.__
    
We can save on typing, share conditionals and share business logic by using the `Validator` and `Result` technique.  Here's what it looks like from the caller's perspective:

    checkWidgetTransfer(transfer).onError(err -> handleError(err));
    //continue

This provides an api for the caller that indicates what an error condition is.  Callers no longer have to guess that an empty string is a pass, and a non-empty string is a fail.  The api provides a place to put error handling, which can take an existing function, or have an on-the-fly lambda in place.  Sweet!

You still have to write up Bob, Carol and Duane's favorite workflow. but things are compact and you don't have to go down many twisty branches, each more a like than the last. 

### Now with a Validator

<img src="https://i.imgur.com/LxHru8gl.jpg" title="Blastoff!"/>

What if you didn't have to write any if/then/else statements?  What if you you only had to write the logic, and something else would handle stringing that logic together.  A validator can make that possible.

Here's what the implementation of `checkWidgetTransfer` looks like, using a validator:

    public static final Result<WidgetTransfer> checkWidgetTransfer(WidgetTransfer transfer) {
        Validator<WidgetTransfer> widgetTransferValidator = new Validator();
        widgetTransferValidator.addRule(suffientAmount, "Insufficient balance to transfer");
        widgetTransferValidator.addRule(parterTransferReqs, "This area is not a transfer eligible area");
        widgetTransferValidator.addRule(dirigibleTransferReqs, "D Category Transferer can only be transferred in transfer area 213");
        widgetTransferValidator.addRule(friendsAndFamilyReqs, "This area is not an eligible area");
        widgetTransferValidator.addRule(internalBlockReqs, "Amount is too small for I type transfer");
        widgetTransferValidator.addRule(internalTotalCapReqs, "This transfer is too large");
        return widgetTransferValidator.validate(transfer); 
    }

The validator can take as many rules as needed, and each rule gets a name and a matching message.  The validator ensures every rule is applied to the transfer, and a `Result` is returned, containing either the error messages or the transfer.

### Implementation Details

[I implemented a `Validator`](https://github.com/monknomo/If-Else-Block-Refactoring/blob/master/src/main/java/com/gunnargissel/suemez/businessrulerefactorexample/refactor5/Validator.java) as a `HashMap` of functions to error strings.  The `validate` method tests each function, and if the test is true, collects the matching message in the `Result`.

[I implemented `Result`](https://github.com/monknomo/If-Else-Block-Refactoring/blob/master/src/main/java/com/gunnargissel/suemez/businessrulerefactorexample/refactor5/Result.java) as an `Either`.  Callers have the option of getting a boolean `hasErrors` or passing in a `Consumer` to `onError`.  The important thing about a `Result` is that it is never null and it guides the developer to the correct method of handling an error.

## Wrap up 

With just a tiny push, we helped our elephant reach orbit.  We've gone from [bog standard spaghetti business logic]() to pure functions embodying composable business logic.  Thank you for coming along for ride.  I welcome comments or feedback at gunnar@gunnargissel.com, or [@monknomo on Twitter](https://twitter.com/monknomo)

<img src="https://i.imgur.com/5Xg3VrRl.jpg"/>

## Credits

_Thank you [Oliver Dodd](https://www.flickr.com/photos/oliverdodd/) for the [elephant](https://flic.kr/p/8N681r)_

_Thank you [NASA, ESA, N. Smith (U. California, Berkeley) et al., and The Hubble Heritage Team (STScI/AURA)](https://www.nasa.gov/multimedia/imagegallery/image_feature_1146.html) for the Carina Nebula_

_[Photo of the shuttle Endeavour](https://flic.kr/p/fejqBW) by [Mr. Littlehand](https://www.flickr.com/photos/73577218@N00/)_

_[Boiler Plate](https://flic.kr/p/Fvyd) [from Les Chatfield](https://www.flickr.com/photos/elsie/)_

_[Blastoff](https://flic.kr/p/q5sdna) by [Matthew Lancaster](https://www.flickr.com/photos/matthew_lancaster_2/)_


