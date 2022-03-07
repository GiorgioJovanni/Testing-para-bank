import json

import requests


class BaseParaBank:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get(self, url):
        headers = {"Accept": "application/json"}
        r = requests.get(url, headers=headers)
        return r

    def post(self, url, headers):
        r = requests.post(url, headers=headers)
        post_response = (json.loads(r.text), r) if r.text else ({}, r)
        return post_response
