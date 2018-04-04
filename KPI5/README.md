### Making the graphs and visuals for https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Resultaten/KPIs/KPI5/KPI5_KB_20-02-2018


The Excel-file [KPI5-KB-AllWebsites_DutchWikipedia-AllNamespaces_20022018_RawData.xlsx](KPI5-KB-AllWebsites_DutchWikipedia-AllNamespaces_20022018_RawData.xlsx) is the master file from which the csv-files in [KPI5-1](KPI5-1) and [KPI5-2](KPI5-2) were derived.

For every KB-website, this Excel contains two sheets. For instance, for the KB-run site [DBNL](http://www.dbnl.org/) the sheet
* _DBNL-Hoofdnaamruimte_ lists which articles in the main namespace (Dutch: _Hoofdnaamruimte_) of Dutch Wikipedia (column A) contain which URLs of the DBNL website (column B)
* _DBNL-Overig_ lists which pages in the other namespaces (Dutch: _Overige naamruimtes_) - mainly Gebruiker:, Help:, Overleg: and Wikipedia: - of Dutch Wikipedia contain which URLs of the DBNL website.
* Column E is the de-duplicated version of column A; it shows all the _unique_ Wikipedia articles  that contain links to the DBNL-site

An overview of all websites of the KB can be found [here](https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Resultaten/KPIs/KPI5/KPI5_KB_20-02-2018#Tabelweergave) . Click on the blue text [weergeven] to open the collapsed table. Alternatively, see [this graph](plot)

The first two sheets in the Excel are the aggegations (=sums) of all the sheets for the individual KB-websites: 
* _AlleDiensten_Hfdnr_ is the aggegate for the main namespace.  [KPI5-KB-DutchWikipedia-MainNamespace_20022018_RawData.csv](KPI5-1/KPI5-KB-DutchWikipedia-MainNamespace_20022018_RawData.csv) in PKI5-1 is the cleaned up version of this sheet.
* _AlleDiensten-Overig_ is the aggegate for the other namespaces
