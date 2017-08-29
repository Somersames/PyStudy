from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as  e:
        return None
    try:
        bsObj=BeautifulSoup(html.read(),"html.parser")
        title =bsObj.body.h1
    except AttributeError as e:
        return None
    return title
# www.pythonscraping.com/pages/page1.html
title=getTitle("http://www.baidu.com")
if title == None:
    print("Title Not Found")
else:
    print(title)