Internet Cash - Kickoff
#######################
:date: 2013-11-27 14:17:00
:author: monknomo
:category: text
:tags: seo, scraping, python, programming, internet cash, business, niche, hn, hacker news, bad idea, scrape, blog
:slug: 2013-11-27-internet-cash-kickoff

.. raw:: html

   </p>

Last week\ `HN`_\  had a post about a\ `blog selling for $36k.`_\  
Ordinarily I'd rate it mildly interesting - blogger does good SEO,
regurgitates a lot of content, sells ads and then\ `sells the
website`_\  for a little over 2x the yearly income.  

.. raw:: html

   </p>

What I found interesting were some of the comments.  `One in
particular`_ pointed out that the site is a manual content aggregator
that could automate most of the aggregation.  The user suggested
auto-scraping the top 100 related sources for new content on a regular
basis, using the `Mechanical Turk`_ to rate and tag each article and
then posting a generated excerpt for each article, tweeting about the
post and posting each picture to pinterest.

.. raw:: html

   </p>

I have a feeling that if a person were to listen to HN and literally do
what the HN folks suggest, that they have a pretty good chance at
something working out.  I plan to test this theory out by taking
plausible-sounding, low-hanging fruit suggestions, like this one, and
trying them out.  What could go wrong?

.. raw:: html

   </p>

For this suggestion, I’ll write a quick feed scraper and article rating
system, put it in a cron job and start automating it.  Using the `MVP`_
style approach, I think I’ll just automate the scraping and make a
rating webapp and do the rating/posting myself at first.  This will let
me get a grip on the most time consuming parts of getting content out on
the web so I have a better idea of what to automate next.  It also
avoids paying the Mechanical Turk until I actually know what I want to
buy.

.. raw:: html

   </p>

.. raw:: html

   </p>

 |Optimistic Scraper|

.. raw:: html

   </p>

What a scraper may look like

.. raw:: html

   </p>

.. _HN: https://news.ycombinator.com/
.. _blog selling for $36k.: https://news.ycombinator.com/item?id=6761234
.. _sells the website: http://amandatinney.com/how-to-sell-a-blog-for-36200/
.. _One in particular: https://news.ycombinator.com/item?id=6763494
.. _Mechanical Turk: https://requester.mturk.com/
.. _MVP: http://en.wikipedia.org/wiki/Minimum_viable_product

.. |Optimistic Scraper| image:: http://farm1.staticflickr.com/149/390131704_cfce9712a5.jpg
   :target: http://www.flickr.com/photos/bigfez/390131704/
