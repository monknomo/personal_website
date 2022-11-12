Title: Why use Docker When You Can Just Use a Fat Jar?
Date: 02/22/2016 19:34
Modified: 02/26/2016 11:00
Category: Operations
Tags: docker, java, jar, containers
Slug: why-use-docker-when-you-can-just-use-a-fat-jar
Author: Gunnar Gissel
Email: monknomo@gmail.com
Summary: Quickly choose whether to use Docker or a self contained fat jar

I saw [a question](https://www.reddit.com/r/java/comments/465sv2) on [r/java](https://www.reddit.com/r/java) that I thought was great.  OP is deploying a fat jar that has everything OP's app requires, so the deploy is just a simple file copy.  OP is also using Docker to deploy the entire environment along with the jar and wonders if it is worth it.

When to Use Docker
---------------------

[Docker](https://www.docker.com/) is great when you are using Docker to deploy your entire server environment.  If you have already container-ized your database, proxy and load balancer, it's a no brainer to add just one more docker image to container-ize your application.  Your team already has the [Docker infrastructure](https://docs.docker.com/registry/deploying/) in place.   Your environment already deploys with Docker.  Unifying procedures keeps things simple.  

### 3 Reasons to Use Docker

1. Your application shrinks and grows. Adding/removing instances helps keep the bills down and the customers happy.  This is particularly important on providers like AWS and DigitalOcean
2. You deploy your application to a lot of different environments. Each different environment needs a couple tweaks to work.
3. You don't want your deployment process to care about the state of server upgrades (like the JVM or Tomcat)


When to Use a Fat Jar
-----------------------

[Fat jars](https://stackoverflow.com/questions/19150811/what-is-a-fat-jar) are great.  A fat jar bundles everything you need into one convenient archive, ready to go.  Deploying a fat jar is easy: copy the jar to the server and run it.  It's worth pointing out that fat jars combine very well with Docker - they are easier to use in the Docker context than containers.

### 3 Reasons to Use a Fat Jar

1. When your environment is hand crafted.  Fat jars are particularly useful both the jar and the environment define configuration
2. When maintaining a Docker registry is significant overhead.  If you're not already doing it, why add yet another infrastructure system?
3. When you have an artifact repository (like [Archiva](https://archiva.apache.org/index.cgi) or [Nexus](https://www.sonatype.com/nexus/solution-overview)).  These make it trivial to grab and deploy a particular version of your fat jar
