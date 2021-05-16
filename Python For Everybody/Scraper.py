# Test Program for Scraping
from bs4 import BeautifulSoup
import requests
def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(productUrl, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'html.parser')
    elems = soup.select('html.js.flexbox.flexboxlegacy.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.applicationcache.svg.inlinesvg.smil.svgclippaths body main.container div.contentArea div#current-conditions.panel.panel-default div#current-conditions-body.panel-body div#current_conditions-summary.pull-left p.myforecast-current-lrg')
    return elems[0].text.strip()

price = getAmazonPrice('https://forecast.weather.gov/MapClick.php?x=171&y=120&site=top&zmx=&zmy=&map_x=171&map_y=120')
print('The Price is ' + price)
