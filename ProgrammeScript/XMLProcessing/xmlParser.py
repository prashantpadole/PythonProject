import csv
import requests
import xml.etree.ElementTree as ET

path="C:\MSDE\PythonProject\ProgrammeScript\XMLProcessing"

def loadRSS():

    url= "https://practicaldatascience.co.uk/feed.xml"


    response = requests.get(url)

    with open(path+"toXMLfile.xml",'wb') as f:
        f.write(response.content)


def parseXML():
  
    # create element tree object
    tree = ET.parse(path+"toXMLfile.xml")
  
    # get root element
    root = tree.getroot()
  
    # create empty list for news items
    newsitems = []
  
    # iterate news items
    for item in root.findall('./channel/item/'):

  
        # empty news dictionary
        news = {}
  
        # iterate child elements of item
        for child in item:
            print(child.text.encode('utf8'))

  
             # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
                print("news[child.tag] : ",news[child.tag],"\n","child.text.encode('utf8') :",child.text.encode('utf8'),"\n")
        #newsitems.append(news)
      
    # return news items list
    #print(newsitems)
    return newsitems

loadRSS()
parseXML()
          