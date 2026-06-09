Title: Projects
Date: 2016-02-08 10:55
Modified: 2016-02-08 10:55
Category: Meta
Tags: open-source, freebies, projects, code, github
Slug: projects
Author: Gunnar Gissel
Summary: I have a few passion projects, like pywe, the Windows Python helper and, notecard-wiki, the wiki for notes

[draw.horse](draw.horse)
=========

This is [a drawing toy](https://github.com/monknomo/draw-this) that I've been working on off and on for a years.  It's inspired by drawing programs from the 80's and 90's that were aimed at kids.  I call it a toy because the intent is not to provide tools to effectively render an image, but to provide various drawing/painting/stamping/interactive features that are fun.  The creation is more the point than the final produce (although my customer's - which is to say my kids - top-demanded feature is a save button).

[Pixel -> SVG Icon Editor](https://monknomo.github.io/pixel-svg-icon-editor/)
==========

This is [a small utility](https://github.com/monknomo/pixel-svg-icon-editor) to help me make pixel-style SVGs in either an 8x8, 16x16, 32x32 or 64x64 grid.  It'll save an SVG made out of little squares, or copy one to your clipboard.  I built it as a little assitant to making buttons for [draw.horse](draw.horse)

[Simple Photo Grid](https://monknomo.github.io/simple-photo-grid/)
=======

[Put an adjustably-sized grid on an image](https://github.com/monknomo/simple-photo-grid).  Zoom into grid squares, and still divide the zoomed in portion of the image into a grid.  I use this for doing watercolors/gouache/sketches from photographs.  Every time I zoom in I say 'enhance' to myself.

[Pretty Good Computer](https://github.com/monknomo/pretty_good_computer)
========================================================================

Pretty Good Computer is a toy computer I built to simulate the [z-machine as described by jgc.](blog.jgc.org/2013/05/the-two-problems-i-had-to-solve-in-my.html) I enjoyed working out the problems long hand, but thought that I could have a computer do the repetetive scut work; they're better at it after all.

The z machine has unlimited memory locations that are numbered, so we can refer to them. The cpu understands 3 instructions:

* `z_n_`
    * `z` zeros, or initializes, the value at memory location `n`
* `i_n_`
    * `i` increments the value at memory location `n`
* `j_n_!m)l`
    * `j` compares memory locations `n` and `m`'s value. If they are equal, the program proceeds to the next line, otherwise it goes to line `l`
    
Of course, I can't figure out a good way to represent infinite memory locations in a browser window, so we are stuck with 16-bits by default. This is user-editable, if you need more space to really explore whatever you are doing.

[Straight-Laced](https://github.com/monknomo/straight-laced)
==============================================================

A theme for [Pelican blogs.](http://blog.getpelican.com/) It's the theme this website is using.  Straight-laced is plain jane, but responsive and marked up with both semantic markup and [schema.org](schema.org) markup.

[CardWiki](https://github.com/monknomo/CardWiki)
=====================================================

[CardWiki](https://github.com/monknomo/CardWiki) is a wiki that is patterned after [TiddlyWiki.](http://tiddlywiki.com/)  Unlike TiddlyWiki, CardWiki is designed with hosting in mind.  CardWiki uses a notecard metaphor, rather than a page metaphor, so you can look at and edit multiple cards at the same time.  If you're the sort of person that likes to keep 100's of tabs open, or you love to accumulate tons of notes on scraps of paper, CardWiki might help you view and organize your thoughts.

Currently, CardWiki is an open source Python project that you can set up and run yourself.  Contact me if you want to see a hosted version of CardWiki

[PyWE](http://www.github.com/monknomo/pywe)
===========

I haven't touched this in ages; I no longer work in a windows shop.  I'm sure there are more modern ways to deal with all this now, but I'm proud of this little collection of batch scripts to deal with multiple python versions and virtual environments on windows boxes.  [PyWE (Python Windows Environment)](http://www.github.com/monknomo/pywe) is a collection of scripts that make it easier to install multiple versions of python, switch between different versions of python and create/activate/deactivate per-python virtual environments.
