Printing from OSX
#################
:date: 2012-03-31 21:06:00
:author: monknomo
:category: text
:tags: printer, linux, mint, samba, mac, osx
:slug: 2012-03-31-printing-from-osx

In retrospect, I should have checked to see if my printer was Mac and
Linux friendly before I bought it...



.. raw:: html

   </p>

As it is, for being an HP, it's been surprisingly easy to get running on
Linux.  I just had to look for network printers.  From the Mac, for some
reason it isn't keen on being discovered or accepting jobs using its
ordinary printer drivers.  The workaround I've been using, which is
ridiculous, is to\ `set up samba`_ to share the printer and to connect
to my fake 'windows' network with the Mac and look for the printer.
 Linux being Linux, I had to use ``sudo smbd restart`` and
``sudo nmbd restart`` instead of ``sudo restart smbd``.  `Whatever`_



.. raw:: html

   </p>

On the plus side, I figured out how to scan to my computer instead of
just to an sd card!  The printer's web interface is half-decent

.. raw:: html

   </p>

.. _set up samba: https://help.ubuntu.com/10.04/serverguide/C/samba-printserver.html
.. _Whatever: http://www.youtube.com/watch?v=Xz7_3n7xyDg
