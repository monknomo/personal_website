Batch File Trick
################
:date: 2011-10-17 13:28:58
:author: monknomo
:category: text
:slug: 2011-10-17-batch-file-trick

Today I learned about batch

 files,

and how to locate the directory they reside

in

from

within the batch file.

The commands that seem relevant are %~d\*n\*, %~p\*n\* and %0

%0 is the program name

%1 is the first command line parameter, and so on until %9

for %~d\*n\* and %~p\*n, n \*is 0-9 and it's meaning corresponds to %0

%~d\*n\* gives the drive letter of %\*n\*

\*%~pn gives the directory of %n\*

\*

\*

%~d\*n\* and %~p\*n \*can be combined into the pretty useful %~dp\*n\*

\*

\*

In terms of practical usage, launching things relative to the batch file
can

work like this:

cd %~dp0

//do stuff relative to the batch file here

or (this technique tries in a variety of ways in an effort to work on

versions of windows going back in the dim mists of the 90's):

%0

cd %0\\..

cd /d %0\\..

//do stuff relative to the batch file here

Using either method directly in a command that needs a relative path can

lead to suboptimal results if the path to the batch file includes
spaces,

for example:

start /B %~dp0jre\\bin\\java more arguments go here

will fail if spaces show up in %~dp0. Depending on what the command is,
it

can be difficult to use quote marks to nip the problem in the bud, so I
tend

to use the above techniques.
