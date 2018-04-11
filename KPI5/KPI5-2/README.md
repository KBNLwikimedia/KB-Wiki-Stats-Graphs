The file [KPI5-KB-Links_Articles_DutchWikipedia-AllNamespaces_20022018_RawData.csv](KPI5-KB-Links_Articles_DutchWikipedia-AllNamespaces_20022018_RawData.csv) has the following fields: 

* _KB-Dienst_: Name of the KB-website (= website that is run and/or managed by the Koninklijke Bibliotheek) 
* _Links_hnr_: Number of links (URLs) to this website in the main namespace of Dutch Wikipedia
* _Artikelen_hnr_: Number of unique articles in the main namespace of Dutch Wikipedia containing (one or more) links to this website 
* _Links_overige_: Number of links (URLs) to this website in the other namespaces of Dutch Wikipedia
* _Artikelen_overige_: Number of unique pages in the other namespaces of Dutch Wikipedia containing (one or more) links to this website 
* _Sortorder_: number used to put the horizontal bars in the desired order

The Jupyther Notebook [KPI5-2.ipynb](KPI5-2.ipynb) visualises the data into a [horizontal barchart](KPI5-Plot2.png). 

![Grafiek: Links en artikelen in Nederlandstalige Wikipedia o.b.v. websites van de Koninklijke Biblioteek](https://raw.githubusercontent.com/ookgezellig/KB-Wiki-Stats-Graphs/master/KPI5/KPI5-2/KPI5-Plot2.png)

This chart has been uploaded to
* https://commons.wikimedia.org/wiki/File:Links_en_artikelen_in_Nederlandstalige_Wikipedia_o.b.v._KB-websites,_hoofdnaamruimte,_20-02-2018.png

and is further explained (in Dutch) on

* https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Resultaten/KPIs/KPI5/KPI5_KB_20-02-2018

You can run this notebook interactively in the cloud via Mybinder.org: https://mybinder.org/v2/gh/ookgezellig/KB-Wiki-Stats-Graphs/master?filepath=KPI5/KPI5-2/KPI5-2.ipynb
