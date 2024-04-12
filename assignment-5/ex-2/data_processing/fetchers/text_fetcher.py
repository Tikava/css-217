import requests

class ResearchArticleFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://ieeexploreapi.ieee.org/api/v1/"

    def search_articles(self, query):
        headers = {'X-API-Key': self.api_key}
        search_url = self.base_url + 'search/articles'
        params = {'queryText': query}
        response = requests.get(search_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            if articles:
                return articles[0]  
        return None

# Example usage:
API_KEY = "YOUR_IEEE_XPLORE_API_KEY"
article_fetcher = ResearchArticleFetcher(API_KEY)
article_info = article_fetcher.search_articles("machine learning")
if article_info:
    print("Title:", article_info.get("title"))
    print("Authors:", ", ".join(article_info.get("authors", [])))
    print("Publication Year:", article_info.get("publicationYear"))
    print("Abstract:", article_info.get("abstract"))
    print("DOI:", article_info.get("doi"))
else:
    print("No articles found.")
