personal_website
================

Repository for my personal business-card-like website.  Contains biographical info

Now with more Pelican!!

Instructions
--------------

these are for windows, using a wsl subsystem.  I personally used Ubuntu.

1. `python -m venv .`
  1. change the line endings to linux style
  1. mess with the classpath so that the script dir is not at c:\, but rather at /mnt/c/etc
  1. copy all the `*.exe` to just plain `*` in the `./Scripts` dir
1. `source .\Scripts\acivate`
  1. test this by trying `python` If it doesn't work, probably have to mess with class path
1. `pip install --upgrade pip`
1. `pip install -r requirements.txt`
  1. At this point you likely have to copy all the new `*.exe` to `*` in the `.Scripts` dir again
1. clone [straight-laced](https://github.com/monknomo/straight-laced) to sibling dir
1. clone [pelican plugins](https://github.com/getpelican/pelican-plugins.git) to sibling dir
1. build with pelican
  1. `pelican -o ./docs`
  1. or, you know, sometimes it seems like `python -m pelican -o ./docs` does the trick, depending on how pip installs stuff
1. view results
  1. run `python serv.py`
  1. navigate to localhost:8080 in the browser
  1. check to see if webpage looks right
