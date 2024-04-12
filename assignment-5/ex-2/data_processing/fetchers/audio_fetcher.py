import requests

class AudioFetcher:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://api.spotify.com/v1/"

    def get_access_token(self):
        auth_url = "https://accounts.spotify.com/api/token"
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(auth_url, data=auth_data)
        access_token = response.json().get("access_token")
        return access_token

    def search_track(self, query):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        search_url = self.base_url + "search"
        params = {
            "q": query,
            "type": "track",
            "limit": 1 
        }
        response = requests.get(search_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get("tracks") and data["tracks"].get("items"):
                track = data["tracks"]["items"][0]
                return {
                    "name": track["name"],
                    "artists": [artist["name"] for artist in track["artists"]],
                    "album": track["album"]["name"],
                    "preview_url": track["preview_url"]
                }
        return None
