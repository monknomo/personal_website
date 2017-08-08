Title: Footnotes!
Slug: footnotes
Date: 8/3/2017 19:00
Modified: 8/3/2017 19:00
Category: Programming
Tags: javascript, design, insidebaseball
Authors: Gunnar Gissel
Summary: Footnotes are cool, but showing footnotes on hover is cooler

<a href="http://imgur.com/yU7tDJn"><img src="http://i.imgur.com/yU7tDJnm.jpg" title="Books! source: imgur.com" /></a>

I was reading away on the internet [when I saw a cool thing.](http://ignorethecode.net/blog/2010/04/20/footnotes/)  Footnotes that popup when you hover over the little <sup id="fnr-footnotes-1">[1](fn-footnotes-1)</sup> note.


Lukas Mathis generously offered his code to the public, so I borrowed the code in his bookmarklet for [Daring Fireball](https://daringfireball.net).  I wasn't quite doing Gruber-style footnotes, which the code assumes.


Gruber Style Footnotes
--------------------------------


A Gruber-style footnote has two parts:


1. The superscript link
2. The footnote with a return link


The superscript link, in Markdown, looks like this: `<sup id="fnr-footnotes-1">[1](fn-footnotes-1)</sup>`.  The important parts are that the `<sup>` element has an id that starts with "fnr" (for "footnote return", I assume), and a link to the footnote that starts with "fn".


The footnote with a return link looks like: `<a id="fn-footnotes-1">1: </a> This is an example footnote here - see how it has a return link [⏎](#fnr-footnotes-1)`.  The important parts are the link with an id that starts with "fn" and the return link to the superscript link's `<sup>` element.


The script I borrowed assumes you have both parts of the Gruber-style footnote, with the appropriate prefixes and return links.


I adjusted the script's color a little to match my theme, but here it is, more or less unchanged from Lukas Mathis' original:


    $(document).ready(function() {
      var sups = document.getElementsByTagName("sup");
      var footnotehtml = [];
      for (var i = 0; i < sups.length; i++) {
        var sup = sups[i];
        if (sup["id"] && sup["id"].substr(0, 3) == "fnr") {
          
          var footnr = sup["id"].substr(3);
          console.log(footnr);
          var footnote = document.getElementById("fn" + footnr);
          console.log(footnote);
          if (!footnote) continue;
          console.log("asdfasdfaf");
          footnotehtml[i] = footnote.parentNode.innerHTML;
          console.log(sup);
          sup.setAttribute("footnoteindex", i);
          sup.onmouseover = function(event) {
            var footnotepopup = document.getElementById("footnotepopup");
            if (footnotepopup) footnotepopup.parentNode.removeChild(footnotepopup);
            var index = parseInt(this.getAttribute("footnoteindex"));
            var popup = document.createElement("div");
            popup.innerHTML = footnotehtml[index];
            popup.id = "footnotepopup";
            popup.style.position = "absolute";
            popup.style.left = event.pageX - 125 + "px";
            popup.style.top = event.pageY + 25 + "px";
            popup.style.width = "15em";
            popup.style.textAlign = "left";
            popup.style.backgroundColor = "Gainsboro";
            popup.style.border = ".1em solid black";
            popup.style.borderRadius = "6px";
            popup.style.padding = "1em";
            document.body.appendChild(popup);
          };
          sup.onmouseout = function(event) {
            var footnotepopup = document.getElementById("footnotepopup");
            if (footnotepopup) footnotepopup.parentNode.removeChild(footnotepopup);
          };
        }
      }
    });






## Footnotes

<a id="fn-footnotes-1">1: </a> This is an example footnote here - see how it has a return link [⏎](#fnr-footnotes-1)

## Credits

_Thank you to [Erica Schoonmaker](https://www.flickr.com/photos/_erica/) for the picture of the [books](https://flic.kr/p/9EUVrx)_