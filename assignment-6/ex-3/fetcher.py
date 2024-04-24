import requests

class Fetcher:
    def __init__(self, url, params):
        self.url = url
        self.params = params
        
    def make_get_request(self):
        return requests.get(url=self.url, params=self.params).json()