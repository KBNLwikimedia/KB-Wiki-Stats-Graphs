import json
import csv
import urllib
from urllib.parse import quote

def read_local_csv(file):
    # Input=local filepath/filename of csv -- Output=List of list
        list = []
        response = open(file, 'r', encoding='utf-8')
        sheet = csv.reader(response, delimiter=';')
        for row in sheet:
            if not str(row).startswith('#', 2):  # skip rows in cvs that start with '#'
                list.append(row)
        return list

def getPageID(wikiTitle):
# Get the pageid of the json call below
#In: Title of wikipedia pag WP:NL
#Out: pageid
    import urllib.request
    with urllib.request.urlopen("https://nl.wikipedia.org/w/api.php?action=query&titles="+ wikiTitle +"&prop=extlinks&format=json&ellimit=500") as url:
        data = json.loads(url.read().decode())
        IDstring= data["query"]["pages"].keys()
        wikiPageID=str(IDstring).split("dict_keys(['")[1].split("'])")[0]
    return wikiPageID

def getExternalLinks(wikiTitle, pageid):
#In: Wikipedia article title (WP:NL) and its pageid
#Out: list of external URLs
    import urllib.request
    with urllib.request.urlopen("https://nl.wikipedia.org/w/api.php?action=query&titles="+ wikiTitle +"&prop=extlinks&format=json&ellimit=500") as url:
        data = json.loads(url.read().decode())
        extLinkList = data["query"]["pages"][pageid]["extlinks"]
    return extLinkList

# def filterURLs(URLlist):
# #  In: list of (mixed; KB and non-KB) URLs
# #  Out: filtered list of URLs, of only KB-websites
#     #List of domains of KB web sites/services, To be used for filtering external urls
#     KBdomains=[".kb.nl", "//kb.nl",
#                ".delpher.nl", "//delpher.nl",
#                ".statengeneraaldigitaal.nl", "//statengeneraaldigitaal.nl",
#                ".geheugenvannederland.nl", "//geheugenvannederland.nl",
#                ".dbnl.org", "//dbnl.org",
#                ".bibliopolis.nl", "//bibliopolis.nl",
#                ".willemfrederikhermans.nl", "//willemfrederikhermans.nl",
#                ".eduperron.nl","//eduperron.nl",
#                ".mennoterbraak.nl","//mennoterbraak.nl",
#                ".mmdc.nl", "//mmdc.nl",
#                ".dbng.nl", "//dbng.nl",
#                ".leesplein.nl", "//leesplein.nl",
#                ".literatuurplein.nl", "//literatuurplein.nl",
#                ".literatuurgeschiedenis.nl", "//literatuurgeschiedenis.nl",
#                ".bibliotheek.nl","//bibliotheek.nl",
#                ".onlinebibliotheek.nl", "//onlinebibliotheek.nl",
#                ".vakantiebieb.nl", "//vakantiebieb.nl",
#                ".digitaleetalages.nl","//digitaleetalages.nl"]
#     filteredURLlist=[]
#     for url in URLlist:
#         for domain in KBdomains:
#            if domain in url: filteredURLlist.append(url)
#     return filteredURLlist

def filterDelpherURLs(DelpherURLlist):
#For Delpher only
#  In: list of (mixed; KB and non-KB) URLs
#  Out: filtered list of URLs, of only Delpher
    #List of Delpher (sub)domains and resolver URLs. To be used for filtering external urls
    # Based on URL patterns from the 3rd column of https://nl.wikipedia.org/wiki/Wikipedia:GLAM/Koninklijke_Bibliotheek_en_Nationaal_Archief/Resultaten/KPIs/KPI9/KPI9_KB_05-02-2020
    DelpherDomains=[
        ".delpher.nl", "//delpher.nl",
        # Newspapers Basiscollectie
        "kranten.kb.nl",
        "resolver.kb.nl/resolve?urn=ddd", "resolver.kb.nl/resolve?urn=ABCDDD",
        "resolver.kb.nl/resolve?urn=KBDDD02", "resolver.kb.nl/resolve?urn=KBNRC01",
        "resolver.kb.nl/resolve?urn=MMCODA01", "resolver.kb.nl/resolve?urn=MMCODA02",
        "resolver.kb.nl/resolve?urn=MMDA03", "resolver.kb.nl/resolve?urn=MMGARO01",
        "resolver.kb.nl/resolve?urn=MMGAVL01", "resolver.kb.nl/resolve?urn=MMHCO01",
        "resolver.kb.nl/resolve?urn=MMKB04", "resolver.kb.nl/resolve?urn=MMKB08",
        "resolver.kb.nl/resolve?urn=MMNIOD05", "resolver.kb.nl/resolve?urn=MMRANM02",
        "resolver.kb.nl/resolve?urn=MMRHCE01", "resolver.kb.nl/resolve?urn=MMSAB03",
        "resolver.kb.nl/resolve?urn=MMSADB01", "resolver.kb.nl/resolve?urn=MMSAEN01",
        "resolver.kb.nl/resolve?urn=MMTRES02", "resolver.kb.nl/resolve?urn=MMVEEN01",
        # Books Basiscollectie
        "boeken.kb.nl",
        "resolver.kb.nl/resolve?urn=dpo", "resolver.kb.nl/resolve?urn=MMKB02",
        "resolver.kb.nl/resolve?urn=MMKB05", "resolver.kb.nl/resolve?urn=MMKB06",
        "resolver.kb.nl/resolve?urn=MMKB11", "resolver.kb.nl/resolve?urn=MMKIT03",
        "resolver.kb.nl/resolve?urn=MMSFUBA02", "resolver.kb.nl/resolve?urn=MMMVC01",
        "resolver.kb.nl/resolve?urn=MMUBL07", "resolver.kb.nl/resolve?urn=MMUBVU02",
        "resolver.kb.nl/resolve?urn=MMUBVU05", "resolver.kb.nl/resolve?urn=MMUBA08",
        # Books Google collectie
        "boeken1.kb.nl",
        # Magazines
        "tijdschriften.kb.nl",
        "resolver.kb.nl/resolve?urn=dts", "resolver.kb.nl/resolve?urn=MMKB07",
        "resolver.kb.nl/resolve?urn=MMKB16", "resolver.kb.nl/resolve?urn=MMRHCG02",
        "resolver.kb.nl/resolve?urn=MMALET01", "resolver.kb.nl/resolve?urn=MMIISG06",
        "resolver.kb.nl/resolve?urn=MMVRED01",
        # Radio bulletins
        "anp.kb.nl",
        "resolver.kb.nl/resolve?urn=anp"]

    filteredDelpherURLlist=[]
    for url in DelpherURLlist:
        for domain in DelpherDomains:
           if domain in url:
               filteredDelpherURLlist.append(url)
    return filteredDelpherURLlist

#=== Main script ==
#Clear file
with open("Delpher_WikiTitles-URLs-Numbers.txt", "w"):
    pass

counter = 1

titleList= read_local_csv("KPI9-08-DelpherTotaal_21-02-2018_05-02-2020.txt")
with open("Delpher_WikiTitles-URLs-Numbers.txt", "a", encoding='utf-8') as myfile:
    myfile.write("LinkNr" + "^^" + "WikiURL" + "^^" + "Delpherlink" + "^^" + "NrOfExtLinks" + "^^" + "NrOfDelpherLinks" + "\n")

    for title in titleList:
        #print(title[0])
        encodedTitle=urllib.parse.quote(title[0]) #http://www.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/
        print(encodedTitle)
        pageid=getPageID(encodedTitle)
        extLinks=getExternalLinks(encodedTitle,pageid)
        extLinkList= [link['*'] for link in extLinks] # List of unfiltered external urls
        numberOfExtLinks = len(extLinkList)

        # Lets filter this list for KB urls
        #KBlinkList=filterURLs(extLinkList)
        #numberOfKBLinks = len(KBlinkList)

        # Lets filter this list for Delpher urls
        DelpherLinkList=filterDelpherURLs(extLinkList)
        numberOfDelpherLinks = len(DelpherLinkList)

        for Delpherlink in DelpherLinkList:
            myfile.write(str(counter)+"^^"+"https://nl.wikipedia.org/wiki/"+title[0].replace(' ','_')+"^^"+Delpherlink+"^^"+str(numberOfExtLinks)+"^^"+str(numberOfDelpherLinks)+"\n")
            print(str(counter)+"^^"+title[0]+"^^"+Delpherlink+"^^"+str(numberOfExtLinks)+"^^"+str(numberOfDelpherLinks))
            counter += 1
    myfile.close()

