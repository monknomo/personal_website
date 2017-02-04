Title: So You Accidentally Got Stuck in vi
Slug: so-you-accidentally-got-stuck-in-vi
Modified: 2/3/2017 19:00
Date: 2/3/2017 19:00
Category: Sysadmin
Tags: sysadmin, command line, command prompt, bash, editor, text editor, how-to, cheatsheet, guide
Authors: Gunnar Gissel
Summary: A cheatsheet with the bare minimum you need to deal with vi


It has happened to all of us.  You're logged into a box, you want to edit some text and boom - vi is the only option.  Or you're on screen and someone is beavering along in vi and then passes you the controls.


What do you do?  How do you quit vi without changing things?  How do you change text with vi?  How do you save with vi?


Sometimes, the after typing a while you notice nothing is changing the way you expect and your cursor is jumping all around.  You are probably stuck in vi.


----------------------------------------------------------------------------------------------------


Noobs Vi Cheatsheet
===================


Vi has this concept of "modes".  Keystrokes behave differently in each mode, so if you aren't sure what mode you are in, mash escape a few times before trying the following commands.


This isn't meant to be exhaustive, just enough to let a programmer dragooned into doing sysadmin stuff to self-rescue


* :q!
    * Quit without saving
* :wq
    * Save and quit
* ZZ
    * Save and quit
* :w
    * Save without quitting
* A
    * Append text to the end of a line
* R
    * Overwrite text starting at the cursor location
* x
    * Delete the character under the cursor
* D
    * Delete to the end of the line
    
-------------------------------------------------------------------------