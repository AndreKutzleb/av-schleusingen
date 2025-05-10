// JavaScript Document

//Copyright by Patrick Steinicke 2003 - www.M-SIGNS.de
//------------------------------------------------------------------

var bilder = new Array
(
"images/01.jpg",
"images/02.jpg",
"images/03.jpg",
"images/04.jpg"
);


var zeit = 5000;
var i = 0;




function diavor()
{
    i++
    if (i == bilder.length)
      {
         i = 0;
      }
	 
document.dia.src = bilder[i];  
}


function diarueck()
{
    i--
    if (i == -1)
      {
         i = bilder.length-1;
      }
	 
document.dia.src = bilder[i];  
}


function zeigen()
{
document.diagr.src = grBilder[i];
}