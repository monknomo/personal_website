Title: How to Move Mercurial Changesets to a New Branch
Slug: how-to-move-mercurial-changesets-to-a-new-branch
Modified: 2/5/2017 11:00
Date: 2/5/2017 11:00
Category: Programming
Tags: mercurial, hg, dvcs, version control, vcs, problem, fix, til
Authors: Gunnar Gissel
Summary: Sometimes you put your code in the wrong branch, but catch it in time to fix it




This is me when I realize I've been committing in the wrong branch all day:


<iframe src="//giphy.com/embed/l41lSR9xZubfd2Qve?html5=true" width="480" height="268" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="giphy.com/gifs/foxtv-office-l41lSR9xZubfd2Qve">via GIPHY</a></p>


Fortunately, there is a way to move changesets between branches, provided you haven't pushed your changes out to any other repositories.  If you have pushed your changes out to the mothership repository, or your coworkers, the only way to pick up the pieces is to get all the users of the repo together and coordinate.  That is beyond to scope of this article, and too hard for all but the smallest or dictatorial teams.


Problem Setup
=============


Here at Reci-p.com we make recipes and sell advertising.  I've been hard at work writing up new recipes.  Here's what I start with:


    $ hg history
    changeset:  1:b1c330d2ac79
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Feb 04 05:15:00 2017 -0900
    summary:    Added quesadilla recipe
    
    changeset:  0:6f5ef8f77a9f
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Jan 28 11:30:00 2017 -0900
    summary:    Added taco recipe
    
I want to add drink recipes, but they aren't ready to show to our valuable users, so I want to add them in a development branch.  Unfortunately, I've been out all night sampling drink recipes and I forget to create the new branch!  


<iframe src="//giphy.com/embed/e3FaCx7T425qg?html5=true" width="480" height="269" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="giphy.com/gifs/e3FaCx7T425qg">via GIPHY</a></p>


This is what I end up with:


    $ hg history    
    changeset:  3:398dfc004270
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Feb 04 05:15:00 2017 -0900
    summary:    Added michela recipe
    
    changeset:  2:852364587134
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Feb 04 05:15:00 2017 -0900
    summary:    Added mojito recipe
    
    changeset:  1:b1c330d2ac79
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Feb 04 05:15:00 2017 -0900
    summary:    Added quesadilla recipe
    
    changeset:  0:6f5ef8f77a9f
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Jan 28 11:30:00 2017 -0900
    summary:    Added taco recipe
    
Fortunately, before I push all my code to the mothership repo, I notice I've been working in the wrong branch.  


Move My Code to a Different Branch
====================================


The approach to fixing this problem is to create the missing branch, then create a patch from my new changesets, apply the patch to the new branch, then strip off the changesets from the incorrect branch.


Working in the same repository as above:


    $ hg export -o patch.diff 3 2
    
I create a patch, which shows up as a file called `patch.diff`.


Create a branch off the newest changeset before I started adding new stuff:


    $ hg update 1
    $ hg branch drinks
    $ hg commit
    
Patch the new branch I just made:


    $ hg import patch.diff
    
This is dangerous, so make sure you are targeting the correct changeset.  You can't easily undo this.  You also need to have [the strip extension enabled](https://www.mercurial-scm.org/wiki/StripExtension)


Remove the changes off the original branch, so we can avoid mixing drink and food recipes:


    $ hg strip 3
    
Phew, my repository is fixed.  Now when look at the history I can see that I've got everything in the correct branch:


    $ hg history -l 4
    changeset:  4:8afca56c4940
    branch:     drinks
    tag:        tip
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Feb 04 05:15:00 2017 -0900
    summary:    Added michela recipe
    
    changeset:  3:357ff9545db
    branch:     drinks
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Feb 04 05:15:00 2017 -0900
    summary:    Added mojito recipe
    
    changeset:  2:357ff9545db
    branch:     drinks
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Feb 04 05:15:00 2017 -0900
    summary:    drinks branch
    
    changeset:  1:b1c330d2ac79
    user:       Gunnar Gissel <gunnar@reci-p.com>
    date:       Sat Feb 04 05:15:00 2017 -0900
    summary:    Added quesadilla recipe
    
Now I'm safe to push and I won't accidentally pollute our recipes with drink mixing recipes


<iframe src="//giphy.com/embed/J4ufHCZTcroys?html5=true" width="480" height="258" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="giphy.com/gifs/party-hard-adventure-time-J4ufHCZTcroys">via GIPHY</a></p>