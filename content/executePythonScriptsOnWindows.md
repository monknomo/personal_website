Title: How to Execute Python Files in Windows CMD
Slug: how-to-execute-python-files-in-windows-cmd
Date: 3/5/2017 13:00
Modified: 3/5/2017 13:00
Category: Programming
Tags: basics, tutorial, how-to, command, prompt
Authors: Gunnar Gissel
Summary: After installing Python, I can't run Python scripts with 'python script.py'.  It's easy to forget to add Python to your path or to forget to restart cmd.

A question I get from new devs fairly frequently is "After installing Python, I can't run Python scripts with 'python script.py'.  What is going wrong?"

The most common thing going wrong is that the Python executable is not on the path.  

Add Python Executable to the Path
=========================

Let's assume your Python executable is `C:\Python37\python.exe`.  Open up cmd.exe and type `setx path "%path$;c:\Python37;c:\Python37\Scripts"`.  This will add both python.exe and the helper scripts included with Python (like pip and easy_install) to the path.

After modifying your path, open a new command prompt (this is important - Windows won't refresh the path in an open command prompt) and then try it out by navigating to your script directory and typing `python script.py`.  You should see your script run!