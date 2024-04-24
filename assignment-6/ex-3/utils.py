import requests

class Fetcher:
    def __init__(self, url):
        self.url = url
        
    def make_get_request(self, params):
        try:
            response = requests.get(url=self.url, params=params)
            response.raise_for_status() 
            return response.json()
        except requests.RequestException as e:
            print("Error making GET request:", e)
            return None
