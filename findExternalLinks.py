import os, os.path, glob
import json
#from pprint import pprint
#from lxml import html
#import requests
import csv
import urllib
from urllib.parse import quote

def finditem(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = finditem(v, key)
            if item is not None:
                return item

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

def filterURLs(URLlist):
#In: list of (mixed; KB and non-KB) URLs
#Out: filtered list of URLs, of only KB-websites
    #List of domains of KB web sites/services, To be used for filtering external urls
    KBdomains=[".kb.nl", "//kb.nl",
               ".delpher.nl", "//delpher.nl",
               ".statengeneraaldigitaal.nl", "//statengeneraaldigitaal.nl",
               ".geheugenvannederland.nl", "//geheugenvannederland.nl",
               ".dbnl.org", "//dbnl.org",
               ".bibliopolis.nl", "//bibliopolis.nl",
               ".willemfrederikhermans.nl", "//willemfrederikhermans.nl",
               ".eduperron.nl","//eduperron.nl",
               ".mennoterbraak.nl","//mennoterbraak.nl",
               ".mmdc.nl", "//mmdc.nl",
               ".dbng.nl", "//dbng.nl",
               ".leesplein.nl", "//leesplein.nl",
               ".literatuurplein.nl", "//literatuurplein.nl",
               ".literatuurgeschiedenis.nl", "//literatuurgeschiedenis.nl",
               ".bibliotheek.nl","//bibliotheek.nl",
               ".onlinebibliotheek.nl", "//onlinebibliotheek.nl",
               ".vakantiebieb.nl", "//vakantiebieb.nl",
               ".digitaleetalages.nl","//digitaleetalages.nl"]
    filteredURLlist=[]
    for url in URLlist:
        for domain in KBdomains:
           if domain in url: filteredURLlist.append(url)
    return filteredURLlist

#=== Main script ==
#Clear file
with open("WikiTitles-URLs-Numbers.csv", "w"):
    pass

counter = 1

titleList= read_local_csv("WikipediaTitles.csv")
for title in titleList:
    #print(title[0])
    encodedTitle=urllib.parse.quote(title[0]) #http://www.compciv.org/guides/python/how-tos/creating-proper-url-query-strings/
    print(encodedTitle)
    pageid=getPageID(encodedTitle)
    extLinks=getExternalLinks(encodedTitle,pageid)
    extLinkList= [link['*'] for link in extLinks] # List of unfiltered external urls
    numberOfExtLinks = len(extLinkList)

    # Lets filter this list for KB urls
    KBlinkList=filterURLs(extLinkList)
    numberOfKBLinks = len(KBlinkList)

    with open("WikiTitles-URLs-Numbers.csv", "a",  encoding='utf-8') as myfile:
        for KBlink in KBlinkList:
            myfile.write(str(counter)+"^^"+title[0]+"^^"+KBlink+"^^"+str(numberOfExtLinks)+"^^"+str(numberOfKBLinks)+"\n")
            print(str(counter)+"^^"+title[0]+"^^"+KBlink+"^^"+str(numberOfExtLinks)+"^^"+str(numberOfKBLinks))
            counter += 1
myfile.close()

