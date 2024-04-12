from dotenv import load_dotenv
import os

load_dotenv()

# Config 
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
youtube_data_api_key = os.getenv("YOUTUBE_DATA_API_KEY")
ieee_xplore_api_key = os.getenv("IEEE_XPLORE_API_KEY")