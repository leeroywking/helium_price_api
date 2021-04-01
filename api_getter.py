from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os


def get_stock_info(key):
    url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
    'id':'5665',
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data["data"]["5665"]["quote"]["USD"]["price"])
        # for item in data["data"]:
        #     if item["id"] == 5665:
        #         # print(item)
        #         return item
        return data["data"]["5665"]["quote"]["USD"]["price"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

if __name__ == "__main__":
    get_stock_info(os.environ.get("COINMARKETAPIKEY"))