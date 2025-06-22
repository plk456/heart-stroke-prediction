from bs4 import BeautifulSoup
import requests

content=requests.get('https://quotes.toscrape.com/')   
print(content)                     
soup=BeautifulSoup(content.text,'html.parser')
print(soup)                         # This statement will print the entire HTML content of the website

s=soup.find_all('a')               # Remove the comments to scrape the anchor tag <a> href link               
for i in s:                                    
    href = i.get('href')
    print(href)



 
