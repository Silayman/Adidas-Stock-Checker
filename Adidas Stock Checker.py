#!/usr/bin/env python3.5
import requests
import json
import time
from bs4 import BeautifulSoup as bs

sku = input("Enter Product ID: ").upper()
locale = input("Enter locale (US/EU/CA): ")
if locale.upper() == "US":
    ending = ".com"
    region = "en_US"
    country = "US"
elif locale.upper() == "EU":
    ending = ".co.uk"
    region = "en_GB"
    country = "GB"
elif locale.upper() == "CA":
    ending = ".ca"
    region = "en_CA"
    country = "CA"

base_url = 'https://www.adidas'
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
                "Accept-Language" : "en-US,en;q=0.8"}

def getVarientStock(sku):
    urlVariantStock = base_url + ending + '/on/demandware.store/Sites-adidas-' + country + "-Site/" + region + '/Product-GetVariants?pid=' + sku
    r = requests.get(urlVariantStock, headers=headers)
    try:
        stock_variations = json.loads(r.text)['variations']['variants']
    except:
        if r.status_code == 404:
            print ("ERROR! " + sku + '" is an invalid PID!')
        elif r.status_code == 403:
            print ("ERROR! IP banned!")
        else:
            print("ERROR! Stock check failed!")
    total = 0
    print("----------------------------")
    print("        PID:"+str(sku)+"           ")

    print("----------------------------")
    for variations in stock_variations:
        total_stock = variations["ATS"]
        total += int(total_stock)
        stockSizes = variations["attributes"]["size"]
        print("Size: " + str(stockSizes) + ". Quantity: " + str(total_stock))
    print("Total stock: " + str(total))
getVarientStock(sku)
