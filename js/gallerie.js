// Slideshow gallery script
// Original by Patrick Steinicke 2003 - www.M-SIGNS.de
// Consolidated and modernized

var zeit = 5000;
var i = 0;
var inter;

function diavor() {
  i++;
  if (i >= bilder.length) {
    i = 0;
  }
  document.dia.src = bilder[i];
}

function diarueck() {
  i--;
  if (i < 0) {
    i = bilder.length - 1;
  }
  document.dia.src = bilder[i];
}
