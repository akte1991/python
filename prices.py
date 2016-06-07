import urllib.request
import time

price = 99.99
while price > 4.75:
    time.sleep(900)
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start = where + 2
    end = start + 4
    price = float(text[start:end])

print(price)



