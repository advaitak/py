# fetch: heading, slug, date of publish from 5 blogs
import requests
from bs4 import BeautifulSoup
url="mention the blog link"
r=requests.get(url)
htmlContent=r.text
#print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)
q=soup.find_all('h2')
for i in q:
 print(i.text)
slug=soup.find_all('h2')
for x in slug:
    print(x.find('a')['href']) 
Date_of_publish=soup.find_all('ul')
for y in Date_of_publish:
    print(y.find('li').text)
