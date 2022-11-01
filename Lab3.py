from hashlib import new
import requests
from bs4 import BeautifulSoup
import smtplib

def data_scraping():
    req = requests.get('https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-128gb-5g-gold-mq083rx-a/pd/D57Y4LMBM/?X-Search-Id=a20ea45cd9585af75906&X-Product-Id=101075749&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view')
    soup=BeautifulSoup(req.text, 'html.parser')
    price=soup.find('p', attrs={'class':'product-new-price'}).text
    new_price=price[0:3]
    new_price=new_price.replace(".","")
    new_price=int(new_price)
    print (price)
    print (new_price)

data_scraping()
