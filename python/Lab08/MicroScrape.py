import requests, re 
from bs4 import BeautifulSoup 
 
data = requests.get("https://www.microcenter.com/product/638579/dell-se2422h-238-fhd-(1920-x-1080)-75hz-hdmi-vga-freesync-flicker-free-led-monitor").content
soup = BeautifulSoup(data, 'html.parser')
details = soup.find("h1")
thisspan = ""
for d in details:
    title = d.find("span")
    if title is not None and title != -1:
        thisspan = title
print("Product %s has a price of %s" % (thisspan.get("data-name"), thisspan.get("data-price")))