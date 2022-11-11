Title: How to Make a Program - Answering 12 Year Old Me's Question
Slug: how-to-make-a-program-answering-12-year-old-mes-question
Date: 7/15/2016 21:08
Modified: 7/15/2016 21:08
Category: Programming
Tags: programming, blast-from-the-past, how-to, tutorial, getting-started, basics
Authors: Gunnar Gissel
Summary: When I was 12, I really wanted to know how to make a program.  Not in the "writing code" sense, but in the mechanical "how do I type words to tell a computer what to do" sense


When I was little, I loved computers.  I thought they were terrifically cool and I really wanted to make them do things.  I had a steady diet of cyberpunk and video games, so I had this idea that you could do anything by jockeying a keyboard and programming.  What I didn't have was any knowledge or resources to get me going.


I wanted to write a program, but I didn't know anybody who had every programmed and the programming books I was able to get my hands on were either ancient and useless (think COBOL manuals) or new and useless (think a late 90's C++ doorstopper).  


I had some idea of how to program.  You write special words, in a really specific order and the computer does something.  Like an excel macro, or something.  What I didn't know is how to turn my words from a text file to something a computer could run.  Like the literal mechanical process of programming.  I was clueless about how to do that.


This was the 90's and I was in Alaska.  Not rural Alaska, but definitely the sticks.  I had the internet, or some reasonable facsimile if nobody needed to make a phone call.  I read [Slashdot](https://slashdot.org/) and forums.  I could read a lot about programming - how people were doing it, what languages were out there, some tutorials here and there.


Everything I read was missing the fundamental steps of how to program.  Sure, they'd tell you how to say "Hello world", but bootstrapping myself up that high with no support network was just not happening.  Maybe I was slow, or I was overthinking it.  It seems like computers are complicated, so why wouldn't creating a program be complicated?


Let me cut to the chase and answer 12 year old me's burning question.  Just in case there is someone out there with the same problem.


How to Make a Program in 4 Simple Steps
-------------------------------------------------------


1. Open a text editor.  A text editor is something like Notepad in Windows or Text Edit in OSX.
2. Write a program.  Just copy paste a hello world program from a tutorial for this step
3. Save this file as a plain text document
4. This is the complicated part that confused me as a kid.  There are two options, depending on the type of language you are using
    1. Compile the file you just saved with a compiler.  Run the resulting executable
    1. Run the file you just saved with an interpreter


That's it!  All you have to do is write a text file and feed it into a compiler or interpreter and you have a program.  Seriously, don't over think this part


### Compilers and Interpreters


I used a couple specialist words in step 4.  12 year old me had read them, but didn't understand them, so I better explain.


A compiler is a thing that takes the text file you wrote and translate it into machine code your computer understands.  Compiled languages are things like C, Java, Go, Rust, [etc.](https://en.wikipedia.org/wiki/Compiled_language)


An interpreter reads the program directly out of the file (or sometimes the command prompt) and 'interprets' the instructions on the fly.  Interpreted languages are things like Python, Javascript, Ruby, Lisp, Perl, [etc.](https://en.wikipedia.org/wiki/Interpreted_language)


Some languages have both a compiler and an interpreter.


The Fine Points
----------------------


It turns out that each language has a variety of fine points, or variations on the 4 steps I listed above.  I'm not going to try to explain everything in a single blog post, but I'll hit the high points for my favorite languages in some later posts.