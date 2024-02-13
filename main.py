# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd 
import requests

url = "https://fakestoreapi.com/products"

new_data = requests.get(url).json()

product_id = []
product_title = []
product_price = []
product_description = []



for get_data in new_data:
    product_id.append(get_data["id"])
    product_title.append(get_data["title"])
    product_price.append(get_data["price"])
    product_description.append((get_data["description"]))
    

print(product_id)
print(product_description)
print(product_price)
print(product_title)

id_series = pd.Series(product_id)
title_series = pd.Series(product_title)
price_series = pd.Series(product_price)
description_series = pd.Series(product_description)

df = pd.DataFrame({
    "id": product_id,
    "title": product_title,
    "price": product_price,
    "description": product_description
})


products = pd.concat([id_series, title_series, price_series, description_series], axis=1)
print(products)

# DataFrame oluşturma
#df = pd.DataFrame(products, columns=["id", "title", "price", "description"])

print(df)

df.to_csv('new.csv', index=False)










