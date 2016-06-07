Title: My First Crack at BEM
Slug: my-first-crack-at-bem
Date: 6/2/2016 20:00
Modified: 6/2/2016 20:00
Category: Learn Along With Me
Tags: javascript, framework, how-to, tutorial, review, web, development, webapp, design-pattern, learn-along
Authors: Gunnar Gissel
Summary: I tried out [bem-tools](https://github.com/bem/bem-tools) to see if I could get the framework working without driving myself crazy.  I also tried a simple “hello world” tutorial and found it somewhat harder than I expected.

[BEM is an interesting concept](https://en.bem.info/) from [Yandex](https://www.yandex.ru/) for managing large/complex webapps html and css.  It’s a really verbose way of assigning css classes to html elements such that everything’s independence is preserved and everything is pluggable and reusable.

Once you get past the [snazzy sales pitch pages,](https://en.bem.info/methodology/) the [documentation](https://en.bem.info/technology/bemhtml/v2/intro/) becomes a little terse, and is more obviously the translated product of busy working programmers.

The team I’m working with is moving away from a big [Flex](https://en.wikipedia.org/wiki/Apache_Flex) app, so I’ve been evaluating a lot of different Javascript frameworks and ways of organizing a project.  Our Flex app is pretty big (round about 100 swfs), and one thing we like about Flex is how it makes reusing components fairly easy.  BEM seems like it offers something similar, in terms of modularity, with perhaps a better organizational structure.

My method of evaluation has been to re-implement one of our medium complexity pages, using different frameworks and styles.  The concept of the page is fairly straightforward - a search, some tabs that display data, and some editing functionality, but it’s big enough and has enough state that it offers some flavor of what it is like to develop in a given framework.

Setting up the BEM Tutorial
------------------------------------------

After reading the “what is BEM” stuff, I dove right into setting up the [“hello world” tutorial.](https://en.bem.info/technology/bemhtml/v2/intro/)  I already have node and github installed, so I fired up gitbash, and started copy pasting.

The first<a id="my-first-crack-at-bem-1-b"></a><sup>[1](#my-first-crack-at-bem-1)</sup> thing I ran into was that `bem server` didn’t quite do what the tutorial said it would.  I expected that command to run a server, so I could check out the demo page, but something went wrong and I had to dive into the documentation to figure out how to actually run a bem server.  For me, the answer was to run `bem server -p 8080 --host=127.0.0.1`.  I assume this is a network or security setting, because the problem seemed to be that a host of `0.0.0.0` wouldn’t work on my machine.

I created a test bundle without an trouble and was able to make a bemjson.js that said “hello BEMHTML” without trouble.  Then I tried the part of the tutorial where we make the “hello world” dynamic via BEMHTML.

At first I was a little confused by what they meant [when they said](https://en.bem.info/technology/bemhtml/v2/intro/#step-4-create-a-template-for-a-greeting)

> Edit `test.bemjson.js`:
>
> `{block: ‘hello’, name: ‘BEMHTML’ }`

I wasn’t sure where I should put the snippet, but then it dawned on me that the tutorial intended me to remove the content field from the ‘hello’ block and add a name field.  Initially I tried to put the entire snippet in the content field. ¯\\\_(ツ)_/¯

I used the `bem create` command to create a directory for the block and “all other necessary files” but was immediately confused, because the tutorial indicates that I should edit the “hello.bemhtml” file, as though it had been newly created.  In my case, it had not been created.  I flailed around for a while, but finally got the hello.bemhtml file created and working the way the tutorial suggested.

After that, the sailing was smooth.

Blazing My Own Way
--------------------------------

At this point, I felt like I had a vague idea of how the BEM tools were intended to be used

* BEMJSON is how you define a page by building it up from blocks
* BEMHTML is BEM’s templating language - it is not how you inject javascript into a page
* i-bem is how you inject javascript into a page (I think)
* BEMTREE isn’t something I’ve figured out a use for as yet.  I assume it’ll come up as I try to make a page that does something.  Or perhaps it is just internal to their templating engine?

After a close reading of the method of BEM, I feel like I have an idea of how to write BEMJSON.  My takeaways were 

1. Blocks can be made of blocks
2. A block should stand on its own, so a block-like sub-part should really be an element
3. You put the contents of a block or element in the content field :)
4. I’m not yet sure how to make a button with an onclick method

As soon as I figure out how to make a button with an onclick method, I’ll post a tutorial. I suspect the answer is contained [here.](https://en.bem.info/technology/bemhtml/v2/intro/#step-7-add-style-and-behavior-css-and-js)  I might also take a crack at improving the “hello world” tutorial for rank beginners, such as myself.

#### Footnotes

<a id="my-first-crack-at-bem-1">1:</a> Well, the real first thing is that I’m on Windows and all the documentation assumes I’m running something Linuxy…  I feel like this is a real problem in the node world.  All us enterprise devs are off in Redmond-land flailing to get stuff made for bash working. [⏎](#my-first-crack-at-bem-1-b)


