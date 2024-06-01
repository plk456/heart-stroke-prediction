from bs4 import BeautifulSoup
import requests

content=requests.get('https://quotes.toscrape.com/')
#print(content)
soup=BeautifulSoup(content.text,'html.parser')
print(soup)
#s=soup.find_all('a')
#for i in s:
#    href = i.get('href')
#    print(href)



 