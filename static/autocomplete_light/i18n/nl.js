/*! Select2 4.1.0-rc.0 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(e){var n;(n=e&&e.fn&&e.fn.select2&&e.fn.select2.amd?e.fn.select2.amd:n).define("select2/i18n/nl",[],function(){return{errorLoading:function(){return"De resultaten konden niet worden geladen."},inputTooLong:function(e){return"Gelieve "+(e.input.length-e.maximum)+" karakters te verwijderen"},inputTooShort:function(e){return"Gelieve "+(e.minimum-e.input.length)+" of meer karakters in te voeren"},loadingMore:function(){return"Meer resultaten laden…"},maximumSelected:function(e){var n="Er "+(1==e.maximum?"kan":"kunnen")+" maar "+e.maximum+" item";return 1!=e.maximum&&(n+="s"),n+" worden geselecteerd"},noResults:function(){return"Geen resultaten gevonden…"},searching:function(){return"Zoeken…"},removeAllItems:function(){return"Verwijder alle items"}}}),n.define,n.require},event=new CustomEvent("dal-language-loaded",{lang:"nl"});document.dispatchEvent(event);