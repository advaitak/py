import requests
from bs4 import BeautifulSoup
url="mention the url"
r=requests.get(url)
htmlContent=r.text
print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)
heading=soup.find_all('h2')
slug=soup.find_all('h2')
date_of_publish=soup.find_all('li')
def function(a,b,c):
  for i in heading:
   print(i.text)
   break
  for x in slug:
   print(x.find('a')['href']) 
   break
  for y in date_of_publish:
   print(y.text)
   break
for z in range(5):
 function(heading,slug,date_of_publish)



