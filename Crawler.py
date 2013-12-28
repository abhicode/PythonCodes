## Simple Crawling Using python & BeautifulSoup

import urlparse
import urllib
from bs4 import BeautifulSoup

urlToSpiderScrap = "http://www.Example.com"
listUrls = [urlToSpiderScrap]
VisitedUrls = [urlToSpiderScrap]

## Remove the Url Whose Content is extracted
while len(listUrls) > 0 :  
    try:
        html = urllib.urlopen(listUrls[0]).read()
    except:
        print "Error".urls[0]    
    soup = BeautifulSoup(html)
    listUrls.pop(0)
    for tag in soup.findAll('a',href=True):
        tag['href'] = urlparse.urljoin(urlToSpiderScrap,tag['href'])
        print tag['href']
        if urlToSpiderScrap in tag['href'] and tag['href'] not in VisitedUrls:
            listUrls.append(tag['href'])
            VisitedUrls.append(tag['href'])
        ## Some Filtering Example
        try:
            parse =  urllib.urlopen(tag['href']).read
            soup_text = BeautifulSoup(ArithmeticEr)
            ## You can filter using tag and attribues
            print len(soup_text.findAll('div',{'class':['price']}))
            ##soup_text.findAll('li') is also filter criteria
            ## For Tag span and class name 'fk-font-17'
            for tag in soup_text.findAll('div',{'class':['price']}):
                print tag.text
                ## print inner text of the tag
        except:
            print ("Cant Parse : ",tag['href'])
