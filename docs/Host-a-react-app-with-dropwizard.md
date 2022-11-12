Title: Host a React App with Dropwizard
Slug: host-a-react-app-with-dropwizard
Date: 5/31/2018 05:45
Modified: 5/31/2018 05:45
Category: Programming
Tags: java, javascript, react, javaee, jersey
Authors: Gunnar Gissel
Summary: Build an api with Dropwizard and a UI with React - then host your UI with your api server.  No proxies needed!

<img src="https://i.imgur.com/R0iywbUl.jpg" alt="drop of water" title="drop of water"/>

Dropwizard is a great Java framework for building RESTful applications.  It helps you quickly set up a server with a RESTful api, and has lots of useful features right out of the box for making production-grade apps.

React is a great Javascript library for building webapps.  Via create-react-app, React comes with excellent tools for running a development server and creating a production build.  The create-react-app production build makes a directory full of static html and Javascript files.  You could host these with Apache, or nginx, or any variety of webservers.  

It is convenient to minimize the number of pieces of infrastructure an application requires, so hosting the static files with the api server is appealing.  The standard way to host static files with Dropwizard is to include them in the jar, so they are accessible from the classpath.  There is no way to externally host static assets out of the box.

Fortunately, some kind souls created the [Dropwizard Configurable Asset Bundle](https://github.com/dropwizard-bundles/dropwizard-configurable-assets-bundle) which allows you to configure an external directory to be hosted at a uri by Dropwizard.

Setup
--------

<img src="https://i.imgur.com/HqQpL3Tm.jpg" alt="origami wizard's duel" title="origami wizard's duel"/>

I've created a [skeletal Dropwizard echo server](https://github.com/monknomo/gravina-dropwizard-configurable-assets-bundle-skeleton) and a [teeny-tiny React app](https://github.com/monknomo/gravina-react-ui) to go with it.  The Dropwizard server is a plain vanilla configuration except for the addition of this dependency in the `pom.xml`

    <dependency>
        <groupId>io.dropwizard-bundles</groupId>
        <artifactId>dropwizard-configurable-assets-bundle</artifactId>
        <version>1.2.2</version>
    </dependency>

and this addition in the `app.yml`

    assets:
      mappings:
        /assets: /
      overrides:
        /: /teeny-tiny-react-app/build

and this change to the configuration class:

    ... extends Configuration implements AssetsBundleConfiguration {
    ...
    @Override
    public AssetsConfiguration getAssetsConfiguration() { return assets; }
    ...

and this addition to the app initialization:

    bootstrap.addBundle(new ConfiguredAssetsBundle("/assets/", "/", "index.html"));

and finally, this addition to the app run command:

    env.jersey().setUrlPattern("/api/*")

###But What Does It Mean?

These configuration changes add the dropwizard-configurable-assets-bundle to your project, assign the `/assets` classpath to the `/` uri, and the `/` uri to the `/teeny-tiny-react-app/build` directory.

They also include a setting that makes Dropwizard look for index.html if nothing matches the incoming uri.

Finally, they host the Dropwizard resources at `/api/*`.

How Do I Use It?
----------------

<img src="https://i.imgur.com/8ZPzPx1m.jpg" alt="bulldozer" title="bulldozer"/>

This configuration allows for two usage modes - development and production.

In development mode, proceed as normal.  Fire up Dropwizard `java -jar muh-sweet-rest-api.jar server app.yml` then move over to your React dev environment and start coding while running `npm run start`.

In production mode, fire up Dropwizard, and then do a React build `npm run build`.  This will create a production-optimized build of your React app, which you can place where Dropwizard expects to find it.

You'll have two options to view your React app - the default https://localhost:3000 or Dropwizard-served https://localhost:8085

The default port is hosted by React's built in server and has all the auto-reloading goodies you are used to.

Dropwizard's port hosts a static build, so it doesn't auto-reload as you code.  It will, however, automatically serve new code if you manually deploy it.

Why should I do this?
------------------------

<img src="https://i.imgur.com/iWsnVTrm.jpg" alt="girl on slide" title="girl on slide"/>

You should do this if:
* You are already running a Java backend
* You want to deploy React changes separately from Java changes
* You have an ops team that will let you touch the war deploy location, but not the html deploy location (or vice-versa)
* Messing with proxying is difficult (environment specific)

You should not do this if:
* You want the frontend and the backend in lockstep
* Proxying is easy
* You already have one or two html servers
* You don't want to use Java

Credits
---------


* _Thank you [Malachi Brown](https://www.flickr.com/photos/malachus/) for the picture of the [wizard's duel](https://flic.kr/p/483B5i)_
* _Thank you [David McGregor](https://www.flickr.com/photos/magilla03/) for the picture of the [water droplet](https://flic.kr/p/c1H69U)_
* _Thank you [Bill Abbot](https://www.flickr.com/photos/wbaiv/) for the picture of the [bulldozer](https://flic.kr/p/bz7oMC)_
* _Thank you [Mel Johnson](https://www.flickr.com/photos/bobandmel/) for the picture of the [kid on the slide](https://flic.kr/p/7s8bR3)_

