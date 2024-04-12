import requests

class VideoFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3/"

    def get_video_info(self, video_url):
        video_id = self.extract_video_id(video_url)
        if not video_id:
            return None
        params = {
            "part": "snippet",
            "id": video_id,
            "key": self.api_key
        }
        search_url = self.base_url + "videos"
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get("items"):
                video_info = data["items"][0]
                return {
                    "title": video_info["snippet"]["title"],
                    "description": video_info["snippet"]["description"],
                    "channel_title": video_info["snippet"]["channelTitle"],
                    "published_at": video_info["snippet"]["publishedAt"]
                }
        return None

    def extract_video_id(self, video_url):
        video_id = video_url.split("=")[-1]
        return video_id