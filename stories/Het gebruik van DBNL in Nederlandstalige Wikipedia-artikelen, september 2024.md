# Het gebruik van DBNL in Nederlandstalige Wikipedia-artikelen, september 2024 
<sup>Olaf Janssen, 27 november 2024</sup>

<img src="https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/images/icon_wp.png" align="right" width="110"  hspace="20"/>

<img src="https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/images/dbnl_logo.png" align="right" width="170" hspace="20"/>

*De Digitale Bibliotheek voor de Nederlandse Letteren ([DBNL](https://www.dbnl.org/)) is een veelgebruikte bron voor artikelen in de Nederlandstalige Wikipedia. In dit artikel kijk ik hoe links (URLs) naar de DBNL-URLs.xxxxx.*

## Sectie over contexct/methode meting URLs in WP, extlinksfidner

dbnl.nl, . be. en .org

https://nl.wikipedia.org/w/index.php?title=Speciaal:VerwijzingenZoeken&limit=100&offset=0&target=https://www.dbnl.org
https://nl.wikipedia.org/w/api.php?action=query&list=exturlusage&eulimit=100&eunamespace=0&format=json&euprotocol=https&euquery=www.dbnl.org


 This function queries the MediaWiki API to find pages in the main namespace
    that contain external URLs matching a specified query.

### Voorbeelden DNL links in WPNL
valt uiteen in 4 groepen
#### Auteurs:  Besopreek DNNb Nl links in artikel albert Verwij 
https://nl.wikipedia.org/wiki/Albert_Verwey 

 https://www.dbnl.org/auteurs/auteur.php?id=verw008

- 
- 3 sjablonen - 
- https://nl.wikipedia.org/wiki/Sjabloon:Infobox_auteur 
- https://nl.wikipedia.org/wiki/Sjabloon:Link_dbnl_auteur 
- https://nl.wikipedia.org/wiki/Sjabloon:Bibliografische_informatie
 
Wikidata : verw008 worst vanuit Wikidata betrokken
https://www.wikidata.org/wiki/Q586323#P723  


#### Teksten: 
#### Titels:
#### Overige : homepage, colofin etc



## Aantal verwijzingen naar DBNL vanuit de Nederlandstalige Wikipedia, gegroepeerd naar DBNL-hoofdcategorie
Als eerste kunnen we kijken hoe vaak er in Nederlandstalige Wikipedia-artikelen verwezen wordt naar pagina's in elk van de drie DBNL-hoofdcategorieën Auteurs, Teksten en Titels.<br/> 
Onderstaande grafiek laat bijvoorbeeld zien dat er (op 5 september 2024) 16.591 URLs in Wikipedia staan die uitkomen op een DBNL-auteurspagina.<br/>
In totaal bevat de Nederlandse Wikipedia 30.768 (niet-unieke) URLs die naar de DBNL linken.

<div style="min-height:652px" id="datawrapper-vis-V8Mmy"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/V8Mmy/embed.js" charset="utf-8" data-target="#datawrapper-vis-V8Mmy"></script><noscript><img src="https://datawrapper.dwcdn.net/V8Mmy/full.png" alt="Donutchart van het aantal verwijzingen (URLs) in Nederlandstalige Wikipedia-artikelen naar DBNL, gegroepeerd per DBNL-hoofdcategorie: Auteurs, Teksten en Titels " /></noscript></div>
<br/>

## Artikelen in Nederlandstalige Wikipedia met meeste links naar DBNL
Top 20 van 18.458 Wikipedia-artikelen

<div style="min-height:625px" id="datawrapper-vis-jaUXc"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/jaUXc/embed.js" charset="utf-8" data-target="#datawrapper-vis-jaUXc"></script><noscript><img src="https://datawrapper.dwcdn.net/jaUXc/full.png" alt="Barchart van de top 20 van artikelen in de Nederlandstalige Wikipedia die de meeste verwijzingen (URLs) naar dbnl.org en dbnl.nl bevatten." /></noscript></div>

Het artikel [de grootr schuowburg]() bevat 442 verwijzingen (URls) naar DBNL
Isreael Querido  23 verwijzingen naar DBNL





## Pagina's in DBNL waarnaar het vaakst verwezen wordt vanuit de Nederlandstalige Wikipedia
Top 20 van 27.875 DBNL-pagina’s

<div style="min-height:643px" id="datawrapper-vis-oek1t"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/oek1t/embed.js" charset="utf-8" data-target="#datawrapper-vis-oek1t"></script><noscript><img src="https://datawrapper.dwcdn.net/oek1t/full.png" alt="Barchart van de top 20 van pagina's in DBNL waarnaar het vaakst verwezen wordt vanuit de Nederlandstalige Wikipedia" /></noscript></div>

naar de [ALL homepage]() wordt 229x verwijzen vanuit WP:NL
[Onze sporyelden deel 3]() 17 verwijzingen vanuit WP:NL



## Nederlandstalige Wikipedia-artikelen die grotendeels op DBNL gebaseerd zijn

<img src="https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/images/Slide_DBNLaggregatieartikelen_05092024.jpg" align="right" width="200"/>

<div style="min-height:514px" id="datawrapper-vis-LDBua"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/LDBua/embed.js" charset="utf-8" data-target="#datawrapper-vis-LDBua"></script><noscript><img src="https://datawrapper.dwcdn.net/LDBua/full.png" alt="Tabel met 17 Nederlandstalige Wikipedia-artikelen die grotendeels op de DBNL gebaseerd zijn. Deze artikel zijn geschreven o.b.v. (bijna) alleen maar DBNL- bronnen. Ze danken hun bestaan (grotendeels) aan de DBNL." /></noscript></div>


Verwijs naar eerder artilel: [Detecting Wikipedia articles strongly based on single library collections.md](Detecting%20Wikipedia%20articles%20strongly%20based%20on%20single%20library%20collections.md)

extlinks_treshhold = 6
linkratio_treshhold = 0.75

Notenapparaaat van CAJ van Dishoeck https://nl.wikipedia.org/w/index.php?title=C.A.J._van_Dishoeck&action=edit 
Dit artikel is geschreven o.b.v. (bijna) alleen maar DBNL- bronnen!



## Onderliggende data op Github
Alle data die gebruikt is in de visualisaties en analyses in dit artikel is beschikbaar op [Github](https://github.com/KBNLwikimedia/KB-Wiki-Stats-Graphs/tree/master/stories/data/DBNL_20240905). Je kunt het Excel-bestand ook [direct downloaden](https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/data/DBNL_20240905/WPNLarticlesAndDBNLUrls_20240905.xlsx).

## Bijbehorende presentatie
<img src="https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/images/Wat_betekenen_DBNL_en_Wikipedia_voor_elkaar-DBNLdag-8November2024.jpg" align="right" width="200"/>

Dit dataverhaal is gebruikt in de presentatie *[Wat betekenen DBNL en Wikipedia voor elkaar?](https://doi.org/10.5281/zenodo.14041711)* tijdens de [viering van 25-jarige bestaan van de DBNL](https://web.archive.org/web/20241105153730/https://www.dbnl.org/dbnldag/) op 8 november 2024. Deze presentatie is beschikbaar op [Zenodo](https://doi.org/10.5281/zenodo.14041711) en [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Wat_betekenen_DBNL_en_Wikipedia_voor_elkaar_-_DBNLdag_-_8November2024.pdf).

## Over de auteur
<img align="left" src="https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/images/389px-Olaf_Janssen_at_GLAM_WIKI_Tel_Aviv_Conference_2018.JPG" width="50" hspace="5"/>

<img src="https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/images/kblogo.png" align="right" width="150"/>

Olaf Janssen is de [Wikimedia-coördinator](https://www.kb.nl/over-ons/experts/olaf-janssen) van de KB, de nationale bibliotheek van Nederland. Hij draagt bij aan [Wikipedia](https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief), [Wikimedia Commons](https://commons.wikimedia.org/wiki/Commons:Koninklijke_Bibliotheek) en [Wikidata](https://www.wikidata.org/wiki/Wikidata:GLAM/Koninklijke_Bibliotheek_Nederland) als [Gebruiker:OlafJanssen](https://nl.wikipedia.org/wiki/Gebruiker:OlafJanssen). ORCID: [0000-0002-9058-9941](https://orcid.org/0000-0002-9058-9941).

## Hergebruik van dit artikel 
De tekst van dit artikel is vrijgegeven onder de [Creative Commons Naamsvermelding](https://creativecommons.org/licenses/by/4.0/deed.nl) CC-BY 4.0 licentie.<br/> 
<img src="images/cc-by.png" width="120" align="right"/>
Citatie: Janssen, Olaf. ‘xxxxxxxxxxx’. Zenodo, 22 november 2024. [https://doi.org/10.5281/zenodo.1xxxx](https://doi.org/10.5281/zenodo.1xxxx). <br/> 
Naamsvermelding: *KB, nationale bibliotheek van Nederland / Olaf Janssen, CC-BY 4.0*

## Persistente identifiers en URLs voor dit artikel
* DOI (Zenodo): [https://doi.org/10.5281/zenodo.xxxxx](https://doi.org/10.5281/zenodo.xxxxx)
* Wikimedia Commons: [https://commons.wikimedia.org/entity/Mxxxxx](https://commons.wikimedia.org/entity/Mxxxxx)
* Github: [https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/xxxxxxxxxxx.html](https://kbnlwikimedia.github.io/KB-Wiki-Stats-Graphs/stories/xxxxxxxxxxx.html)

