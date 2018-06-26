#### 1) Main namespace of WP:NL

The file [WPNLHoofdnaamruimteArtikel-KBdienst-KBurl_definitief_20022018.txt](WPNLHoofdnaamruimteArtikel-KBdienst-KBurl_definitief_20022018.txt) lists which articles in (the main namespace of) Dutch Wikipedia contain which URLs of websites of the Koninlijke Bibliotheek, as measured on 20-02-2018. 
* The 'ZZZZ' in this file is used as a seprator, as more traditonal separators (, ; - etc) are not safe, they can also occur in the URLs. 
* The middle column tells to which KB-website the URL is related (Delpher Kranten Basis, DBNL, GvN etc.)
* It is the exact same file as in [KPI5-1](../KPI5-1)

The Jupyther Notebook [KPI5-2-Hoofdnaamruimte.ipynb](KPI5-2-Hoofdnaamruimte.ipynb) does two things:  

1) First, it takes the txt-file to generates a Pandas Dataframe with the following fields: 

* _KBLabel_: Short name/label of the website. This label is also used in the middle colomn of the above txt-file  
* _KBFullname_: Long name of the website. You see this name on the vertical axis of the barchart plot below
* _NumLinks_hnr_: Number of links (URLs) to this website in the main namespace of Dutch Wikipedia
* _NumWPArtikelen_hnr_: Number of unique articles in the main namespace of Dutch Wikipedia containing (one or more) links to this website 
* _Sortorder_: number used to put the horizontal bars in the desired order

2) Next, it visualises this dataframe into a [horizontal barchart](KPI5-Plot2_hoofdnaamruimte.png). 

![Grafiek: Links en artikelen in (de hoofdnaamruimte van) de Nederlandstalige Wikipedia o.b.v. websites van de Koninklijke Biblioteek](https://raw.githubusercontent.com/ookgezellig/KB-Wiki-Stats-Graphs/master/KPI5/KPI5-2/KPI5-Plot2_hoofdnaamruimte.png)

This chart has been uploaded to
* https://commons.wikimedia.org/wiki/File:Links_en_artikelen_in_Nederlandstalige_Wikipedia_o.b.v._KB-websites,_hoofdnaamruimte,_20-02-2018.png

and is further explained (in Dutch) on

* https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Resultaten/KPIs/KPI5/KPI5_KB_20-02-2018

You can run this notebook interactively in the cloud via Mybinder.org: https://mybinder.org/v2/gh/ookgezellig/KB-Wiki-Stats-Graphs/master?filepath=KPI5/KPI5-2/KPI5-2-Hoofdnaamruimte.ipynb

#### 2) Other namespaces of WP:NL (combined)
In the exact same way, but now for all the other namespaces of WP:NL combined, using the notebook [KPI5-2-OverigeNaamruimtes.ipynb](KPI5-2-OverigeNaamruimtes.ipynb) on the data [WPNLOverigeNaamruimtes-KBdienst-KBurl_definitief_20022018.txt](WPNLOverigeNaamruimtes-KBdienst-KBurl_definitief_20022018.txt) gives us the plot [KPI5-Plot2_overigenaamruimten.png](KPI5-Plot2_overigenaamruimten.png).
