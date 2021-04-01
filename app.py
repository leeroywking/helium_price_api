import flask
import requests
import os
from api_getter import get_stock_info

COINMARKETAPIKEY = os.environ.get("COINMARKETAPIKEY")

# print(COINMARKETAPIKEY)

helium_data = get_stock_info(COINMARKETAPIKEY)
# print("Here is your helium data\n",helium_data)
helium_price_USD = helium_data["quote"]["USD"]["price"]
print("and here is your helium price", helium_price_USD)

