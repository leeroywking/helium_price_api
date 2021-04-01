from flask import Flask
app = Flask(__name__)
import requests
import os
from api_getter import get_stock_info
from webhook_to_slack import send_to_slack
COINMARKETAPIKEY = os.environ.get("COINMARKETAPIKEY")

# print(COINMARKETAPIKEY)

# helium_data = get_stock_info(COINMARKETAPIKEY)
# # print("Here is your helium data\n",helium_data)
# helium_price_USD = helium_data["quote"]["USD"]["price"]
# print("and here is your helium price", helium_price_USD)

@app.route("/ed89d968-3acb-4818-ad82-c8fd9f5447e5-c627154e-be84-48f3-af89-7c4878777d4c")
def helium():
    COINMARKETAPIKEY = os.environ.get("COINMARKETAPIKEY")
    helium_data = get_stock_info(COINMARKETAPIKEY)
    helium_price_USD = helium_data["quote"]["USD"]["price"]
    helium_price_USD = helium_price_USD * 100 // 1 / 100
    send_to_slack(helium_price_USD)
    return str(helium_price_USD)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)