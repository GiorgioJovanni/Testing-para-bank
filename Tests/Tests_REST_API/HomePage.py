import json

import requests


class ParaBankHomePage:
    def get(self, url):
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)
        return response

    def post(self, url):
        headers = {"Accept": "application/json"}
        response = requests.post(url, headers=headers)
        return response
