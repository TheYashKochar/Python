# Program to scrape an item from Flipkart.com
from bs4 import BeautifulSoup
import requests
def getFlipkartPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(productUrl, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'html.parser')
    elems = soup.select('html.fonts-loaded body div#container div div._2c7YLP.UtUXW0._6t1WkM._3HqJxg div._1YokD2._2GoDe3 div._1YokD2._3Mn1Gg.col-8-12 div._1AtVbE.col-12-12 div.aMaAEs div.dyC4hf div.CEmiEU div._25b18c div._30jeq3._16Jk6d')
    return elems[0].text.strip()

price = getFlipkartPrice('https://www.flipkart.com/oppo-f19-pro-fluid-black-128-gb/p/itmf3153ba8dbf1a?pid=MOBGYV9VCE8G2SDV&lid=LSTMOBGYV9VCE8G2SDVKROOXV&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=hp_bannerads_5_2.bannerAdCard.BANNERADS_OPPO_8GLI3NJYMWFJ&fm=organic&iid=47d599af-9ff6-4d98-93e5-f100c122b4cd.MOBGYV9VCE8G2SDV.SEARCH&ppt=hp&ppn=homepage&ssid=1xrnusv29jlvzz7k1616492670573')
print('The Price is ' + price)
