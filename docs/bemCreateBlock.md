Title: How the Hell Do I Create a New Block and Look at It?
Slug: how-the-hell-do-i-create-a-new-block-and-look-at-it
Date: 06/06/2016 19:30
Modified: 06/06/2016 19:30
Category: Learn Along With Me
Tags: javascript, framework, how-to, tutorial, review, web, development, webapp, design-pattern, learn-along
Authors: Gunnar Gissel
Summary: It's not immediately obvious how to make the basic building blocks with BEM.  Once you have created some blocks, you'll want to see them in the browser, and that is also not immediately obvious

To create a block, use the bem-tools command `bem create -l whatever.level.this.goes.to -b my-block-name`

I have yet to develop a good organizational ontology<a id="bem-new-blocks-1-b"></a><sup>[1](#bem-new-blocks-1)</sup> for naming levels, so your guess is as good as mine as to what the best practices are for naming levels.

Blocks seem easier to name, as they are generally some kind of structure.  I've been using things like “button" or “title" or “search-bar" or “advanced-search" for names.

Once you've created blocks and have a bundle you want to look at<a id="bem-new-blocks-2-b"></a><sup>[2](#bem-new-blocks-2)</sup>, what do you do?

You run the bem server!  The bem documentation says running `bem server` works, but in my case, I need to specify the ip address.  I also specify the port, because I run a lot of different things on my workstation.  For example:

`bem server -p 8080 --host=127.0.0.1`

Once you've done that, browse to https://127.0.0.1:8080 and you should see the bem server index page giving you diagrams of your bundles and links to your bundles' index pages

#### Footnotes

<a id="bem-new-blocks-1">1:</a>I'm not at all certain I'm using 'ontology' correctly, but I'm cribbing from [wikipedia](https://en.wikipedia.org/wiki/Ontology) and the [w3c](https://www.w3.org/TR/vocab-org/) so at least I *look* smart. [⏎](#bem-new-blocks-1-b)

<a id="bem-new-blocks-2">2:</a> What is a bundle?  I don't really know, but I think it roughly maps to a 'web page' - look out for a future blog post. [⏎](#bem-new-blocks-2-b)

