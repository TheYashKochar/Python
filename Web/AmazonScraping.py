# Program to Scrape an item from Amazon
from bs4 import BeautifulSoup
import requests
def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(productUrl, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'html.parser')
    elems = soup.select('#priceblock_dealprice')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Apple-iPhone-XR-Fully-Unlocked/dp/B07P839TX1/')
print('The Price is ' + price)
