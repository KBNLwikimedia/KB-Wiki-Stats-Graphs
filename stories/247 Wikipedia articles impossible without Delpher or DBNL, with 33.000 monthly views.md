# 247 Wikipedia articles impossible without Delpher or DBNL, with 33.000 monthly views
Latest update: 20 May 2020

*This post ... purpose.... * 

### Quiz time:

*What is the connection between a garbage man, a garbage bag and a garbage truck?*<br/>
<image src="images/garbage-2354422_960_720.jpg" height="150"/> <image src="images/220px-Vuilniszak.jpg" height="150"/>
 <image src="images/260px-Eboueurs_20100508_Aix-en-Provence_1.jpg" height="150"/>

*Or between the Dutch soccer players Cor van der Gijp, Gerrie ter Horst and Joop van Daele?*<br/> 
<image src="images/Cor_van_der_Gijp_1954b.jpg" height="150"/> <image src="images/266px-Sparta_tegen_Ajax_2-1,_Cruijff_in_duel_met_Ter_Horst_(l),_Bestanddeelnr_920-0595.jpg" height="150"/> <image src="images/Joop_van_Daele_(1976).jpg" height="150"/>

*Or between Hotel De Indes and the Internationaal Press Museum, both located in The Hague, The Netherlands?*<br/>
<image src="images/DenHaagHotelDesIndes.JPG" height="150"/> <image src="images/266px-Den_Haag_-_Javastraat_32_(2018).jpg" height="150"/>

*Or between a children's song book and the litarary magazine 'Forum' (1932-1935)?<br/>
<image src="images/260px-Heije-kinderliederen-1847.jpg" height="150"/> <image src="images/for003193201_01_tpg.jpg" height="150"/>

### Answer:

Zonder Delpher of DBNL zouden er over deze dingen zeer waarschijnlijk geen Wikipedia-artikelen bestaan! (@maaikenapolitano, @mirjamraaphorst)

M.a.w. : de inhoud van deze artikelen is geheel of grotendeels gebaseerd op inhoud uit Delpher en/of DBNL. Ze hebben hun bestaan te danken aan de KB als contentleverancier, en de Wikipedia-gemeenschap die al die stukjes Delpher/DBNL-content samenvoegen tot artikelen voor een breed publiek.
Hoe zit dit precies?

Elke twee jaar meet ik een aantal indicatoren over het bereik en hergebruik van de KB-collectie via de Wikimedia-platformen. In februari was het weer zover, ik zal daarover in latere Plein-posts nog uitgebreid verslag doen. Maar één van de inzichten die ik kreeg wil ik nu al graag met jullie delen: er staan op Wikipedia tientallen artikelen die er zonder Delpher en DBNL niet zouden zijn geweest.



<image src="images/image_10658527031588781879393.png" width="150"/>
<image src="images/image_11235458251588782175115.png" width="150"/>
<image src="images/image_12425167721588761061236.png" width="150"/>
<image src="images/image_2194896221588784171279.png" width="150"/>
<image src="images/image_68690689531588266794442.png" width="150"/>
<image src="images/image_78079566521588266716668.png" width="150"/>
<image src="images/imagetools0.png" width="150"/>
<image src="images/imagetools1.png" width="150"/>
<image src="images/imagetools2.png" width="150"/>
<image src="images/imagetools3.png" width="150"/>
<image src="images/imagetools4.png" width="150"/>

Iets specifieker, afgelopen februari heb ik gemeten

    Welke artikelen op de Nederlandstalig Wikipedia één of meer verwijzingen naar KB-diensten bevatten, met name naar Delpher en DBNL. De inhoud van deze artikelen is m.a.w. gedeeltelijk of geheel gebaseerd op inhoud uit deze KB-diensten. (meer info)
    Hoe vaak die artikelen gemiddeld per maand worden opgevraagd (meer info)
    Hoeveel KB-bronvermeldingen er in al die Wikipedia artikelen zitten. (meer info)
    Eén artikel kan immers meerdere bronvermeldingen bevatten. Dit zie je heel duidelijk in het artikel over Hotel De Indes, dat maar liefst 74 verwijzingen naar Delpher Kranten bevat.

Tijdens dit meetproces begon het me op te vallen dat er aardig wat Hotel Des Indes-achtige artikelen zijn: artikelen die opvallend veel links naar met name Delpher en DBNL bevatten. Dat wekte mijn nieuwsgierigheid, dus ik ben er eens wat dieper en systematischer ingedoken.....
Aanpak in 4 stappen
Stap 1

Eerst heb ik een inventarisatie gemaakt van alle artikelen op (de Nederlandstalige) Wikipedia die één of meer links naar Delpher of DBNL bevatten. Dat doe je met dit tooltje, daar stop je een URL (of eigenlijk een URL-patroon) in, en je krijgt dan een lijst van artikelen waarin dat URL-patroon voorkomt. Onderstaande screenshot van dat tooltje is gebaseerd op de URL https://www.delpher.nl (klik voor live tool)

Als je dit tooltje gebruikt voor alle Delpher-urls (vergeet daarbij resolver-urls zoals http://resolver.kb.nl/resolve?urn=ddd niet!, zie kolom 3 van deze tabel voor alle gebruikte url-patronen) en vervolgens de resulterende lijsten samenvoegt, ontdubbelt en omzet naar Excel, krijg je uiteindelijk een lijst van zo'n 6800 artikelen waarin een of meerdere Delpher-urls voorkomen.

Een vergelijkbaar proces voor DBNL (url-patroon http(s)://*.dbnl.org) levert een lijst van ruim 7600 unieke Wikipedia-artikelen op.
Stap 2

Toen ik eenmaal die artikellijsten had, heb ik voor elk artikel bepaald welke (en hoeveel) externe links het precies bevat, en bepaald welke van die links naar Delpher (of DBNL) wijzen. Dit heb ik gedaan m.b.v. van de MediaWiki API en een Python script (voor Delpher en voor DBNL). In onderstaand screenshot van het Delpher-script zie je dat er gefilterd wordt op o.a. de resolver-urls van de Delpher Kranten Basiscollectie.

Deze stap levert dan uiteindelijk een Excel op die er (voor Delpher) als volgt uitziet:

In bv. het artikel ...die_Revolutie_niet_begrepen!... zitten dus 16 externe links waarvan er 9 naar Delpher wijzen.
Stap 3

Omdat we op zoek zijn naar artikelen die geheel of grotendeels gebaseerd op zijn op inhoud uit Delpher (of DBNL), is het vervolgens nuttig om naar de zgn. linkratio te kijken. Dat is de verhouding tussen het totaal aantal externe links, en het aantal daarvan dat naar Delpher verwijst. Een linkratio van 1,00 betekent dat alle externe links in een artikel Delpher-links zijn. Hoe lager de linkratio, deze kleiner het relatief aantal Delpher-links in het artikel.
Stap 4

Om vervolgens te bepalen of een artikel zijn bestaan grotendeels te danken heeft aan Delpher (of DBNL) hanteer ik twee drempelcriteria:

    Het artikel moet een minimum aantal externe links bevatten, want de inhoud moet in voldoende mate gebaseerd zijn op externe bronnen.
    De linkratio moet boven een bepaalde drempel uitkomen, om zo voldoende vaak Delpher (DBNL) als externe bron te hebben.

In de keuze van beide drempels zit enige vrijheid, ik heb de volgende gehanteerd:

    voor Delpher: Aantal externe links >=6, linkratio>=0.75
    voor DBNL: Aantal externe links >=4, linkratio>=0.7

Voor Delpher krijg je dan dit:

Bevindingen

De zo gevonden artikelen zijn plekken waar sterke aggregatie en herpublicatie van Delpher-content plaatsvindt. Met andere woorden: In dit soort artikelen wordt informatie uit Delpher over personen, plaatsen, gebeurtenissen en andere onderwerpen voor een miljoenenpubliek samengebracht. Idem voor DBNL.

Als je de zo verkregen overzichten van 'aggregatie-artikelen' bekijkt, zie je

Voor Delpher

    Er zijn 193 artikelen die hun bestaan (grotendeels) aan Delpher te danken hebben.
    Het artikel Lijst van historische Nederlandse netnummers bevat de meeste Delpher-links, 165 van de 195 externe links, met bovengenoemde Hotel Des Indes op de 2e plaats.
    De onderwerpsbreedte van artikelen die Delpher als hoofdbron gebruiken is opvallend groot: van het vuilniswezen tot sjieke hotels, van politici tot ter dood veroordeelden, en van muziekprijzen tot sterrenrestaurants.
    Artikelen over sport - o.a. voetballers, jaaroverzichten van zwemkampioenschappen en korfbal - maken veelvuldig gebruik van Delpher, evenals lijsten van burgemeesters.

Voor DBNL

    Er zijn 54 artikelen die hun bestaan grotendeels aan DBNL te danken hebben.
    Joost van den Vondel bevat de meeste DBNL-links, 32 van de 44 in totaal.
    Vooral artikelen die te maken hebben met Nederlandse letterkunde, schrijvers, boeken, dichters, literatuur ed. maken gebruik van DBNL als hoofdbron. De onderwerpsbreedte van op DBNL gebaseerde artikelen is een stuk kleiner dan die van Delpher. Dit zijn gezien de inhoud en thematiek van DBNL geen verrassingen.

    Elke maand 33.000 views

    Leuk en aardig, al die Wikipedia-artikelen waarin de inhoud van Delpher (DBNL) voor een breed publiek beschikbaar wordt gemaakt, maar worden die artikelen nou ook een beetje gelezen? Ook dat heb ik uitgezocht.

    Het bovengenoemde tooltje geeft voor elk artikel ook het aantal opvragingen (pageviews) in een bepaalde periode, in dit geval is dat (bijna) 2 jaar van 21-02-2018 t/m 05-02-2020.

Hierdoor kunnen we het totaal aantal opvragingen van deze 193 Delpher- en 54 DBNL-aggregatieartikelen in die twee jaar bepalen.

    Voor Delpher: 343.821 pageviews
    Voor DBNL: 445.713 pageviews

Opgeteld komt dit dus neer op 789.534 pagewiews, oftewel 33.000 opvragingen per maand.

Omdat dit opvragingen zijn van 'pure, onverdunde' KB-content - weliswaar buiten de eigen diensten - kunnen deze extra pageviews onverkort bij de bestaande KB-indicatoren over publieksbereik opgeteld worden (zie ook hier) (@frankbergsma @elsbethk @trudiestoutjesdijk)

Achterliggende data

Bovenstaande uitleg is ook beschikbaar op Wikipedia. De achterliggende data zijn beschikbaar als Excel in de bijlagen, en op Github:

    Lijst van Delpher aggregatieartikelen
    Lijst van DBNL aggregatieartikelen



