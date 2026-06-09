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
