Confluence and Tomcat and Firewalls
###################################
:date: 2012-11-29 14:44:00
:author: monknomo
:category: text
:tags: linux, confluence, wiki, tomcat, ufw, firewall, troubleshooting
:slug: 2012-11-29-confluence-and-tomcat-and-firewalls

|Port Blocking|



.. raw:: html

   </p>

I was trying to upgrade my home install of Confluence today, when I ran
into an unexpected error shutting it down.



.. raw:: html

   </p>

.. raw:: html

   <p>

    

    .. raw:: html

       </p>

    SEVERE: Catalina.stop: 

    

    .. raw:: html

       </p>

    java.net.ConnectException: Connection refused

    

    .. raw:: html

       </p>

    blah blah blah, stacktrace

    

    .. raw:: html

       </p>

    .. raw:: html

       <p>



.. raw:: html

   </p>

A little googling and it looks like most people who encounter this error
were trying to stop a Tomcat that had never started or a Tomcat that was
trying to use a port that was already in use.  Neither was the case for
me.



.. raw:: html

   </p>

tldr; much troubleshooting later, I found an `answer`_.  My firewall was
blocking port 8005, which Tomcat needs to shutdown.



.. raw:: html

   </p>

I fixed it with



.. raw:: html

   </p>

.. raw:: html

   <p>

    

    .. raw:: html

       </p>

    sudo ufw allow from 127.0.0.1 to 127.0.0.1 port 8005

    

    .. raw:: html

       </p>

    .. raw:: html

       <p>

.. raw:: html

   </p>

.. _answer: http://stackoverflow.com/questions/5698802/apache-tomcat-java-net-connectexception-connection-refused

.. |Port Blocking| image:: http://i.imgur.com/NG8Cj.jpg
