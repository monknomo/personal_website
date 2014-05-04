One More Thing
##############
:date: 2012-03-31 10:45:00
:author: monknomo
:category: text
:tags: linux, mint, os, alsa, sound, drivers, nvidia
:slug: 2012-03-31-one-more-thing

This is more so I remember than anything, but after I loaded the Nvidia
drivers for the AT5ION-I, my sound quit working.



.. raw:: html

   </p>

I fixed it by \ ``sudo nano /etc/modprobe.d/alsa-base.conf`` and
adding \ ``options snd-hda-intel probe_mask=0xffff,0xfff2`` at the
bottom of the file.  I also made sure I had digital audio selected under
the Hardware tab  and HDMI selected under the Output tab in the Sound
Configuration panel.  A reboot was required to get it all to work.

.. raw:: html

   </p>

