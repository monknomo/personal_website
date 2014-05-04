Github on Windows
#################
:date: 2013-11-19 10:57:00
:author: monknomo
:category: link
:tags: git, github, workaround, windows
:slug: 2013-11-19-github-on-windows

`via`_

.. raw:: html

   </p>

The github Windows app is pretty slick, except that it doesn’t seem to
want to let changes to the global config stick. I have the problem where
I can’t clone a repository from Windows because I have a self signed ssl
 cert in the certificate chain between me and github
 (GitHub.IO.ProcessException:Cloning into ‘jogging-ledger’…fatal: unable
to access ‘SSL certificate problem: self signed certificate in
certificate chain). I can’t do anything about the self signed cert, but
supposedly there is a setting that fixes the problem: “git config
--global http.sslVerify false”

.. raw:: html

   </p>

Using this setting lets me clone, push and pull from the command line.
It even works from the github Windows app *until I close and reopen it*.

.. raw:: html

   </p>

I can see the problem with the ‘git config --global --edit’ command.
 The [http] entry in the global configuration file is emptied out when
the github Windows app restarts. I end up with a useless chain of
“[http] [http] [http]” I can’t seem to find a setting in the gui that
prevents this emptying so I used “git config --local http.sslVerify
false” to set each individual repository.  This makes cloning a little
harder, since I have to remember to use the global setting before
attempting to clone, but gets the job done.

.. raw:: html

   </p>

//dang, I've got to figure out how to email tumblr so that the
linebreaks don't go all wonky

.. raw:: html

   </p>

.. _via: https://github.com/monknomo/jogging-ledger.git/':
