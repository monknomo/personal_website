Title: HTML Form Anti-Patterns
Slug: html-form-anti-patterns
Date: 6/1/2016 21:00
Modified: 6/1/2016 21:00
Category: Opinion
Tags: javascript, web, development, webapp, design-pattern, anti-pattern, bad, naughty
Authors: Gunnar Gissel
Summary: HTML forms are everywhere, but people keep doing horrible things to users with them.  

This is a list of bad things people do with forms on web pages.  If you do any of these things, you should not only feel bad, you should **change it!**

Losing Data When Users Go Back (or Forward)
-----------------------------------------------------------------------

Look, people think they should be able to navigate around the web.  They want to go forward, backwards, up, down wherever.  They _will_ get to your form and want to check something on the page they came from.  They will leave your form half filled out and when they come back and they have to type everything again, they will drop kick their computer out the window and send you the bill.

How many users do you lose because your form doesn’t remember what they typed?  I bet you don’t know, because if you do this you don’t bother logging user behavior.

When a user navigates away from a form you should hang onto what they typed for a loooong time.  However long you think is reasonable, multiply it by 7.

Losing Data on Validation
----------------------------------------

Validation is great, everyone should validate user input to their server.  What nobody should ever do is tell the user they gave you something “bad” and then ditch everything they just spent ten minutes typing out.  Someone just tried to engage with you, to have a meaningful conversation with you(!) and you kicked them in the teeth for splitting an infinitive.

[TODO taking out the trash gif]

When a form fails server side validation **DO NOT THROW AWAY THE USER’S DATA!**  You have their data.  Just give it back to them with some red text or a message telling them how to fix whatever it is you need fixed.

Modal Dialogs as Form Validation Messages
-----------------------------------------------------------------

Sometimes you really want to get a user’s attention.  You may be tempted to use a modal dialog to display form validation messages.

No. Don’t. Stop. [TODO get a willy wonka gif for here]

Especially don’t do this on focus lost from each field.  People need to tab around


Inappropriate Security Level
-------------------------------------------

You need to actually think about what level of security your form needs.  If the form you designed just collects people’s addresses, social security numbers, bank passwords and mother’s maiden names, you need a high level of security.  You should _not_ remember data in this form forever, and maybe not remember it at all.

Hell, data like that should probably be trapped behind a login before the user even gets to enter it.

If you’re writing a form like the vast majority of the internet is composed of - that is to say trivial nonsense that nobody but you cares about - you don’t need a high level of security.  Please save this data forever (or however long the user is likely to walk away and come back to the computer).

If you have a mix of sensitive and inane data, do the sensible and kind thing - make two forms.  The first form should require no login and should only have inane data and should keep it forever.  The second form should be behind a login and keep the data only as long as your security requirements dictate.

And for the love of god, if their logged in session expires, don’t just kick them back to your homepage and throw away all their work without an awfully good reason.



