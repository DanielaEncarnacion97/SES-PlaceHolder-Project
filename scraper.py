#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml
import json
import urllib.parse
import re

import pprint

def get_walmart(product):
    product = product.strip().lower()
    url = f'https://www.walmart.com/search/?query={product}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')


    bs4_titles = soup.select('.search-result-product-title > .product-title-link')
    bs4_prices = soup.select('.price-group')


    titles = []
    prices = []

    for bs4_title in bs4_titles:
        titles.append(bs4_title.attrs.get('title', 0))
    for bs4_price in bs4_prices:
        prices.append(bs4_price.get_text())


    output = list()

    for i in range(len(titles)):
        try:
            title = titles[i]
            title = title.strip()

            price = prices[i]
            price = price.lower().strip()
            price = price.replace('$', '')
            price = price.replace('¢', '')
            price = float(price)

            output.append((title, price))
        except Exception:
            pass

    output.sort(key=lambda x: x[1])


    return output

def get_target(product):
    product = product.strip().lower()

    url = f'https://redsky.target.com/recommended_products/v1?placement_id=slp&pricing_store_id=2867&keyword={product}&purchasable_store_ids=2867%2C2545%2C2072%2C1221%2C1875&visitor_id=016F8BDE3808020197139914D1B502FA&key=eb2551e4accc14f38cc42d32fbc2b2ea'
    response = requests.get(url)
    data = json.loads(response.text)

    output = list()

    for product in data.get('products', []):
        try:
            title = product.get('title', '')

            # Take into account `&`  character
            title = title.replace('&#38;', '&')
            title = re.sub('&#\d+; ?', '', title)

            price = product['price'].get('formatted_current_price', 0)
            price = price.lower().strip()
            price = price.replace('$', '')
            if '¢' in price:
                price = price.replace('¢', '')
                price = float(price)
                price *= 1/100
            price = float(price)

            output.append((title, price))
        except Exception:
            pass

    output.sort(key=lambda x: x[1])

    return output

if __name__ == "__main__":
    pprint.pprint(get_walmart('electronics'))
    pprint.pprint(get_target('electronics'))

