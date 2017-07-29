Title: Changing an Uncontrolled Input to Controlled Error in React
Slug: changing-an-uncontrolled-input-to-controlled-in-react
Date: 07/29/2017 10:35
Modified: 07/29/2017 10:35
Category: Programming
Tags: react, newb, learning
Authors: Gunnar Gissel
Summary: My react linter kept giving me an error and nothing I changed in javascript fixed it.  A quick excursion to the server solved all my problems


<img src="http://i.imgur.com/gAbkVMzl.jpg"/>


React wants form inputs and the like to keep their state inside React, inside of inside the input.  This style is called a "controlled input".  They also offer "uncontrolled input" where the input manages its own state.


React apparently does not like inputs switching from controlled to uncontrolled.  I was developing a form with the docs open next to my editor and I kept getting a `Warning: CustomInput is changing an uncontrolled input of type text to be controlled. Input elements should not switch from uncontrolled to controlled (or vice versa). Decide between using a controlled or uncontrolled input element for the lifetime of the component. More info: `[https://fb.me/react-controlled-components](https://fb.me/react-controlled-components)


As far as I could tell, my input was set up to always be controlled.  I changed javascript around and googled for quite some time before realization set in


## I was Switching a Form Value from `''` to `null`


This is apparently a _no-no_ in React's controlled component land.  My initial state set up had all empty strings, and the only subsequent state manipulation was to get data from webservices.  The webservices I'm working with return a fairly faithful representation of data from a database - nulls and all.


I solved it by converting my state variable to `const` in the render method - with a twist:


    const nullable = this.state.nullable == null ? '' : this.state.nullable;


A little sprinkling of last minute converters and all is well.

_Thank you [Sebastian Dooris](https://www.flickr.com/photos/sebastiandooris/) for the [sprinkles](https://flic.kr/p/61ZqoU)_