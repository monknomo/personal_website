Title: TIL CSS has a 'Calculate' Function
Slug: til-css-has-a-calculate-function
Date: 02/07/2017 21:00
Modified: 02/07/2017 21:00
Category: TIL
Tags: til, css, html, web development, web dev, web
Authors: Gunnar Gissel
Summary: CSS will let you add different units together, but you have to use the calc() function


I don't like to specify layouts in pixels, because display sizes are all over the place.  I dislike sniffing the display size and adjusting parameters through javascript, because I feel like the document should take care of all of that for me.


Something that has been bothering me is I find myself specifying heights, widths, margin, etc in em, while I typically specify border in px.  Maybe this is bad practice, but it's what I've been doing.


The trouble is when trying to figure out how big something is, I can add up the em, and I can add up the pixels, but I didn't know how to combine them.


Today I learned that you can combine them with the calc() function.  `calc( 10em + 5px );` will spit out the number.


It's only supported in bleeding edge browsers, but it's a nice feature.


The big gotcha is that you _must_ have a space surrounding the mathematical operator, or it won't get parsed.


Happy Calculating!