import requests


class BaseParaBank:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get(self, url):
        headers = {"Accept": "application/json"}
        r = requests.get(url, headers=headers)
        return r
