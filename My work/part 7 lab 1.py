# Write a program to print this JSON to the console.
# https://api.coindesk.com/v1/bpi/currentprice.json 
# then modify the program to only output the current price in Euros.

# Author: Grace Mary Smyth

import requests  
url ="https://api.coindesk.com/v1/bpi/currentprice.json" 
response = requests.get(url) 
data = response.json()
# print(data) 
print(data['bpi']['EUR']['rate_float']) 