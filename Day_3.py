from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("https://baike.baidu.com/item/Python/407313?fr=aladdin")
bsObj=BeautifulSoup(html,"html.parser")
# url =bsObj.findAll("a",{"href":re.compile("item")})
# for text in url:
#     print(text["href"])
url = bsObj.findAll("a")
for link in url:
    if 'href' in link.attrs:
        print(link.attrs["href"])