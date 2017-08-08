Title: Turn Your Spaghetti Code into Functions
Slug: turn-your-spaghetti-code-into-functions
Date: 03/16/2017 19:15
Modified: 03/16/2017 19:15
Category: Programming
Tags: java, technique, diy, how-to, tutorial, guide, lambda, function, refactor
Authors: Gunnar Gissel
Summary: How functions can help you refactor complex branching code.  Through the magic of functions, you can get rid of if-else trees and switch statements!

Business rules are the bane of a developer's existence, yet are the bread and butter of their career.  Business rules are your business's money-makers and form the essence of your business's being.

And yet, business rules are often tacked into a program with a big mega-class worth of `if/else` statements.  It is often hard to read business rule code and even harder to figure out what it is supposed to be doing.  Further, the OO way of encapsulating business rules is either fundamentally inadequate, or so widely misunderstood by working developers that the common pattern is a god class that mutates everything it touches.

Anyone who has worked on a 'mature' set of business rules knows that untangling what is going on is extremely hard.  Here's a set of techniques for making the code easier to follow, so you can put your effort into understanding your stakeholders and making sure what's in the code is what they _want_ to be in the code.

Here's an example of standard Java business logic that evaluates a business object (`BusinessTransfer`) and creates messages to return to the user if it violates business rules:

    public static final String checkWidgetTransfer(WidgetTransfer transfer) {
        String businessRuleErrors = "";

        if (transfer.getTransferer().getAccount(transfer.getFromAccount()).getBalance().compareTo(transfer.getAmount()) > 0) {
            businessRuleErrors += "Insufficient balance to transfer ; ";
        }

        if (transfer.getTransferTypeCode().equals("200")) {
            if (!transfer.getAreaCode().matches("907|412|213")) {
                businessRuleErrors += "This area is not a transfer eligible area. ; ";
            } else if (transfer.getAreaCode().matches("213")) {
                if (transfer.getTransferer().getCategory().equals("D")) {
                    businessRuleErrors += "D Category Transferer can only be transferred in transfer area 213. ; ";
                }
            }
        } else if (transfer.getTransferTypeCode().equals("710")) {
            if (!transfer.getAreaCode().matches("574|213|363|510")) {

            }
        }

        if (!transfer.getTypeCode().equals("I")) {
            if (!isBlockSize(transfer)) {
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
    
The above example is inspired by actual code running in the wild.  It's hard to read.  Effectively reading it takes knowledge of what a "200" transfer type code is or what is acceptable data for different transfer area codes.  The parantheses are nested, which makes copy-pasting (a common technique developers use to work with this style of code) perilous.  A dev can't afford to miss a single curly bracket without causing a hard to debug problem.
    
Logic Block Paradigm Shift
---------------------------

A quick way of refactoring long branching `if/else` code is to dispense with branches and with `elses`.  By rephrasing each business rule into a positive constraint, a developer can check to see if the constraint conditions are met, rather than walking a branching logic tree.  This technique increases line count a little, but improves readability a lot.

    public static final String checkWidgetTransfer(WidgetTransfer transfer) {
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

The above code is much cleaner.  Each business rule is contained in its own block of logic, and all the properties needed to determine whether a condition has been met are named.

### The Bad

Business knowledge of what codes mean is still required.  What is a "200" transfer type code?  The code doesn't say, so hopefully it is documented somewhere...
    
And Now, With Predicates
-------------------------

The `if/else` blocks can be made more readable by creating predicates out of the logic they represent.  Predicates can be named, which allows developers to name rules in a way that allows for clear discussions with even non-technical users.

    static final Predicate<WidgetTransfer> suffientAmount = trans -> trans.getTransferer().getAccount(trans.getFromAccount()).getBalance().compareTo(trans.getAmount()) > 0;
    static final Predicate<String> isPartner = ttc -> ttc.equals("200");
    static final Predicate<String> isFriendsAndFamily = ttc -> ttc.equals("710");
    static final Predicate<String> isFriendAndFamilyDiscountLegal = ac -> ac.matches("574|213|363|510");
    static final Predicate<String> isPartneringArea = ac -> ac.matches("907|412|213");
    static final Predicate<String> isDirigibleArea = ac -> ac.matches("213");
    static final Predicate<String> isDirigibleCategory = cat -> cat.equals("D");
    static final Predicate<String> isInternal = tc -> tc.equals("I");

    public static final String checkWidgetTransfer(WidgetTransfer transfer) {
        String businessRuleErrors = "";

        String transferTypeCode = transfer.getTransferTypeCode();
        String areaCode = transfer.getAreaCode();
        String category = transfer.getTransferer().getCategory();
        String typeCode = transfer.getTypeCode();

        if (suffientAmount.test(transfer)) {
            businessRuleErrors += "Insufficient balance to transfer ; ";
        }

        if (isPartner.test(transferTypeCode)
                && isPartneringArea.negate().test(areaCode)) {
            businessRuleErrors += "This area is not a transfer eligible area. ; ";
        }

        if (isPartner.test(transferTypeCode)
                && isDirigibleArea.test(areaCode)
                && isDirigibleCategory.test(category)) {
            businessRuleErrors += "D Category Transferer can only be transferred in transfer area 213. ; ";
        }

        if (isFriendsAndFamily.test(transferTypeCode)
                && isFriendAndFamilyDiscountLegal.negate().test(areaCode)) {
            businessRuleErrors += "This area is not an eligible area. ; ";

        }

        if (isInternal.negate().test(typeCode)
                && !isBlockSize(transfer)) {
            businessRuleErrors += "Amount is too small for I type transfer. ; ";
        }

        if (isInternal.negate().test(typeCode)
                && isTotalOverCap(transfer)) {
            businessRuleErrors += "This transfer is too large. ; ";
        }

        return businessRuleErrors;
    }
    
### The Good

Each `if` block is readable in something approximating "business English".  The rules are defined as predicates, which are both portable and reusable.  The predicates that make up the rules are also individually testable, without having to test all of them at once.

### The Bad

This technique still uses `&&` which is not idiomatic with functions in Java.  While the predicates that make up the rules are portable, the rules themselves are made of multiple predicates and are not portable.  Nothing has been done that can't be done with ordinary methods.
    
Predicate Chaining
---------------------

Changing the predicates to all take BusinessTransfer as an argument eliminates the need to create named property variables and also allows for chaining predicates together.

    static final Predicate<WidgetTransfer> suffientAmount = trans -> trans.getTransferer().getAccount(trans.getFromAccount()).getBalance().compareTo(trans.getAmount()) > 0;
    static final Predicate<WidgetTransfer> isPartner = trans -> trans.getTransferTypeCode().equals("200");
    static final Predicate<WidgetTransfer> isFriendsAndFamily = trans -> trans.getTransferTypeCode().equals("710");
    static final Predicate<WidgetTransfer> isFriendAndFamilyDiscountLegal = trans -> trans.getAreaCode().matches("574|213|363|510");
    static final Predicate<WidgetTransfer> isPartneringArea = trans -> trans.getAreaCode().matches("907|412|213");
    static final Predicate<WidgetTransfer> isDirigibleArea = trans -> trans.getAreaCode().matches("213");
    static final Predicate<WidgetTransfer> isDirigibleCategory = trans -> trans.getTransferer().getCategory().equals("D");
    static final Predicate<WidgetTransfer> isInternal = trans -> trans.getTypeCode().equals("I");
    static final Predicate<WidgetTransfer> isBlockSize = trans -> isBlockSize(trans);
    static final Predicate<WidgetTransfer> isTotalOverCap = trans -> isTotalOverCap(trans);

    public static final String checkWidgetTransfer(WidgetTransfer transfer) {
        String businessRuleErrors = "";

        if (suffientAmount.test(transfer)) {
            businessRuleErrors += "Insufficient balance to transfer ; ";
        }

        if (isPartner.and(isPartneringArea.negate()).test(transfer)) {
            businessRuleErrors += "This area is not a transfer eligible area. ; ";
        }

        if (isPartner.and(isDirigibleArea).and(isDirigibleCategory).test(transfer)) {
            businessRuleErrors += "D Category Transferer can only be transferred in transfer area 213. ; ";
        }

        if (isFriendsAndFamily.and(isFriendAndFamilyDiscountLegal.negate()).test(transfer)) {
            businessRuleErrors += "This area is not an eligible area. ; ";
        }

        if (isInternal.negate().and(isBlockSize.negate()).test(transfer)) {
            businessRuleErrors += "Amount is too small for I type transfer. ; ";
        }

        if (isInternal.negate().and(isTotalOverCap.negate()).test(transfer)) {
            businessRuleErrors += "This transfer is too large. ; ";
        }

        return businessRuleErrors;
    }
    
Almost Fully Functional (mutates businessRuleErrors):

    static final Predicate<WidgetTransfer> suffientAmount = trans -> trans.getTransferer().getAccount(trans.getFromAccount()).getBalance().compareTo(trans.getAmount()) > 0;
    static final Predicate<WidgetTransfer> isPartner = trans -> trans.getTransferTypeCode().equals("200");
    static final Predicate<WidgetTransfer> isFriendsAndFamily = trans -> trans.getTransferTypeCode().equals("710");
    static final Predicate<WidgetTransfer> isFriendAndFamilyDiscountLegal = trans -> trans.getAreaCode().matches("574|213|363|510");
    static final Predicate<WidgetTransfer> isPartneringArea = trans -> trans.getAreaCode().matches("907|412|213");
    static final Predicate<WidgetTransfer> isDirigibleArea = trans -> trans.getAreaCode().matches("213");
    static final Predicate<WidgetTransfer> isDirigibleCategory = trans -> trans.getTransferer().getCategory().equals("D");
    static final Predicate<WidgetTransfer> isInternal = trans -> trans.getTypeCode().equals("I");
    static final Predicate<WidgetTransfer> isBlockSize = trans -> isBlockSize(trans);
    static final Predicate<WidgetTransfer> isTotalOverCap = trans -> isTotalOverCap(trans);
    
    static final Predicate<WidgetTransfer> parterTransferReqs = trans -> isPartner.and(isPartneringArea.negate()).test(trans);
    static final Predicate<WidgetTransfer> dirigibleTransferReqs = trans -> isPartner.and(isDirigibleArea).and(isDirigibleCategory).test(trans);
    static final Predicate<WidgetTransfer> friendsAndFamilyReqs = trans -> isFriendsAndFamily.and(isFriendAndFamilyDiscountLegal.negate()).test(trans);
    static final Predicate<WidgetTransfer> internalBlockReqs = trans -> isInternal.negate().and(isBlockSize.negate()).test(trans);
    static final Predicate<WidgetTransfer> internalTotalCapReqs = trans -> isInternal.negate().and(isTotalOverCap.negate()).test(trans);
    
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
            businessRuleErrors += "This area is not an eligible area. ; ";
        }

        if (internalBlockReqs.test(transfer)) {
            businessRuleErrors += "Amount is too small for I type transfer. ; ";
        }

        if (internalTotalCapReqs.test(transfer)) {
            businessRuleErrors += "This transfer is too large. ; ";
        }

        return businessRuleErrors;
    }
    
Using a Validator:

    static final Predicate<WidgetTransfer> suffientAmount = trans -> trans.getTransferer().getAccount(trans.getFromAccount()).getBalance().compareTo(trans.getAmount()) > 0;
    static final Predicate<WidgetTransfer> isPartner = trans -> trans.getTransferTypeCode().equals("200");
    static final Predicate<WidgetTransfer> isFriendsAndFamily = trans -> trans.getTransferTypeCode().equals("710");
    static final Predicate<WidgetTransfer> isFriendAndFamilyDiscountLegal = trans -> trans.getAreaCode().matches("574|213|363|510");
    static final Predicate<WidgetTransfer> isPartneringArea = trans -> trans.getAreaCode().matches("907|412|213");
    static final Predicate<WidgetTransfer> isDirigibleArea = trans -> trans.getAreaCode().matches("213");
    static final Predicate<WidgetTransfer> isDirigibleCategory = trans -> trans.getTransferer().getCategory().equals("D");
    static final Predicate<WidgetTransfer> isInternal = trans -> trans.getTypeCode().equals("I");
    static final Predicate<WidgetTransfer> isBlockSize = trans -> isBlockSize(trans);
    static final Predicate<WidgetTransfer> isTotalOverCap = trans -> isTotalOverCap(trans);
    
    static final Predicate<WidgetTransfer> parterTransferReqs = trans -> isPartner.and(isPartneringArea.negate()).test(trans);
    static final Predicate<WidgetTransfer> dirigibleTransferReqs = trans -> isPartner.and(isDirigibleArea).and(isDirigibleCategory).test(trans);
    static final Predicate<WidgetTransfer> friendsAndFamilyReqs = trans -> isFriendsAndFamily.and(isFriendAndFamilyDiscountLegal.negate()).test(trans);
    static final Predicate<WidgetTransfer> internalBlockReqs = trans -> isInternal.negate().and(isBlockSize.negate()).test(trans);
    static final Predicate<WidgetTransfer> internalTotalCapReqs = trans -> isInternal.negate().and(isTotalOverCap.negate()).test(trans);
    
    public static final Result<WidgetTransfer> checkWidgetTransfer(WidgetTransfer transfer) {
        Validator<WidgetTransfer> widgetTransferValidator = new Validator();
        widgetTransferValidator.addRule(suffientAmount, "Insufficient balance to transfer.");
        widgetTransferValidator.addRule(parterTransferReqs, "This area is not a transfer eligible area.");
        widgetTransferValidator.addRule(dirigibleTransferReqs, "D Category Transferer can only be transferred in transfer area 213.");
        widgetTransferValidator.addRule(friendsAndFamilyReqs, "This area is not an eligible area.");
        widgetTransferValidator.addRule(internalBlockReqs, "Amount is too small for I type transfer.");
        widgetTransferValidator.addRule(internalTotalCapReqs, "This transfer is too large.");
        return widgetTransferValidator.validate(transfer);
    }  