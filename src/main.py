from ckin_api_controller import CkinController
from pprint import pprint
import json

if __name__ == "__main__":

    url = 'https://data.gov.il'
    params = {
        'resource_id':'ecfff372-8e52-43da-99e8-3f73cb053c62',
        'limit':'10000'
    }
    con = CkinController(url, params)
    con.request_data()
    # pprint()