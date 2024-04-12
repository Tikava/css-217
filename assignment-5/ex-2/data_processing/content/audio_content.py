class AudioContent:
    def __init__(self, name, artists, album, preview_url):
        self.name = name
        self.artists = artists
        self.album = album
        self.preview_url = preview_url

    def __str__(self):
        return f"Audio Content: Name={self.name}, Artists={', '.join(self.artists)}, Album={self.album}, Preview URL={self.preview_url}"
