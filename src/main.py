import ckan_api_controller as ckan
from pprint import pprint
import json

if __name__ == "__main__":

    url = 'https://data.gov.il'
    params = {
        'resource_id':'ecfff372-8e52-43da-99e8-3f73cb053c62',
        'limit':'10000'
    }
    con = ckan.CkanController(url, params)
    # con.request_data()

    ckan.ckan_to_dataframe(con.request_data())
