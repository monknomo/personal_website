The Triplesec Diary - First Draft
#################################
:date: 2013-12-15 16:37:06
:author: monknomo
:category: text
:tags: programming, javascript, encryption, security, triplesec.js, triplesec, diy, make, mvp
:slug: 2013-12-15-the-triplesec-diary-first-draft

|image|

.. raw:: html

   </p>

.. raw:: html

   </p>

I've knocked out a `first usable draft`_ of the `encrypted diary`_ I
started on earlier in the weekend and only have\ `a bit more digging to
go.`_  It could use some polish, maybe an undo feature, definitely some
keyboard shortcuts, but it makes a diary, encrypts it and saves it to
local storage.

.. raw:: html

   </p>

Now I just need to write up an interactive tutorial for user's without a
diary/a diary with no entries, and it'll be ready for folks to look at.

.. raw:: html

   </p>

I mentioned in the earlier post that I couldn't figure out how to get
the text out of the epiceditor - this is the trick:

.. raw:: html

   </p>

.. raw:: html

   <p>

.. code:: prettyprint

    editor.getElement('editor').body.innerHTML 

.. raw:: html

   </p>

|image|

.. raw:: html

   </p>

I've been thinking of new features I might like and have a couple ideas

.. raw:: html

   </p>

#. A settings panel with:
#. Some themes
#. The option to delete a whole diary
#. The option to change your passphrase and re-encrypt your diary
#. Support for multiple diaries
#. Exporting/importing encrypted diaries
#. Optionally hosting encrypted diaries on a server for inter-browser
   portability

.. raw:: html

   </p>

*Thanks to `The National Library of Scotland`_ and `ㇹヮィㇳ`_ for their
generously CC licensed photos*

.. raw:: html

   </p>

.. _first usable draft: http://gunnargissel.com/triplesecdiary/triplesecdiary.html
.. _encrypted diary: http://blog.gunnargissel.com/post/69994259505/triple-y-encrypted-journal
.. _a bit more digging to go.: https://github.com/monknomo/The-Triplesec-Diary
.. _The National Library of Scotland: http://digital.nls.uk/first-world-war-official-photographs/pageturner.cfm?id=74462370
.. _ㇹヮィㇳ: http://www.flickr.com/photos/shirokazan/

.. |image| image:: https://31.media.tumblr.com/719a026d3d6cccce94b54af33c052560/tumblr_inline_mxvlcfm3Nc1r1fwt3.jpg
   :target: http://digital.nls.uk/first-world-war-official-photographs/pageturner.cfm?id=74549618
.. |image| image:: https://31.media.tumblr.com/34998a11437a803052aae3cb9f0f53da/tumblr_inline_mxvlgcC0F51r1fwt3.jpg
   :target: http://www.flickr.com/photos/shirokazan/3008143555/in/photolist-5zPwh4-5GB6ib-5He8mX-98FKDH-7Gyc17-aBAf5A-bti5oM-aHSytg-95xYCe-8uiXKc-dXeppF-9yUQVT-dXemYF-dXeocx-daQzYj-daQxcV-daQAso-bsbfYb-7Yku1Z-95xZKt-9yXRq9-9yUQoV-9yXRtG-9yUPZP-9yXRuU-9yXRdS-9yUQTt-9yUQJP-9yXRU9-9yUQc8-9yUQC6-9yXRGC-9yUPNF-9yUQma-9yUQhk-9yXRSw-daQxHe-9yXRjG-9yUQd2-9yUQ7P-9yUQ8T-9yUQP8-9yUQ6p-9yXRHL-9yUQk4-9yXR1u-bxNpH9-9yUQiH-9yXRK3-9yXRsf-9yXRQb/
