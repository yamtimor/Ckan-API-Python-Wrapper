import requests
import json
from pprint import pprint
from ckan_logger import logger
from ckan_exceptions import CkanAPIConnectionError,CkanAPIResponseError


class CkanController:

    def __init__(self, base_url: str, params: dict = None):
        self.base_url = base_url
        self.params = params
        self.logger = logger
        # self.records = list()
        self.api_uri = '/api/3/action/datastore_search'

    def request_data(self, decoder = 'utf-8'):
        records = list()
        try:
            response = requests.get(f'{self.base_url}/{self.api_uri}', params=self.params)
            data = json.loads(response.content.decode(decoder))
            while len(data['result']['records']) != 0:
                if response.ok:
                    self.logger.info('Connected successfully to API')
                    records += data['result']['records']
                    print(data['result']['_links']['next'])
                    print(len(data['result']['records']))
                else:
                    self.logger.error('Got invalid response from API. Status: %s',response.status_code)
                    raise CkanAPIResponseError

                response = requests.get(f'{self.base_url}{data["result"]["_links"]["next"]}')
                data = json.loads(response.content.decode(decoder))
        except Exception:
            self.logger.exception('Failed to connect Ckan API')
            raise CkanAPIConnectionError

        return records


    def get_data(self):
        pass