
from data_processing.creator import DataProcessorCreator
from data_processing.processors.audio_processor import AudioDataProcessor
from data_processing.processors.text_processor import TextDataProcessor
from data_processing.processors.video_processor import VideoDataProcessor
from data_processing.data import Data
from data_processing.fetchers.audio_fetcher import AudioFetcher
from data_processing.fetchers.video_fetcher import VideoFetcher
from data_processing.fetchers.text_fetcher import ResearchArticleFetcher
from config.config import spotify_client_id, spotify_client_secret, youtube_data_api_key, ieee_xplore_api_key


def main():
    
    audio_fethcer = AudioFetcher(spotify_client_id, spotify_client_secret)
    video_fetcher = VideoFetcher(youtube_data_api_key)
    text_fetcher = ResearchArticleFetcher(ieee_xplore_api_key)

    processor_creator = DataProcessorCreator()

    print("Choose data type to process:")
    print("1. Text")
    print("2. Audio")
    print("3. Video")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        query = input("Enter the title of article you want to find: ")
        article_info = text_fetcher.search_articles(query)
        if (article_info):
            data = Data("text", article_info)
            processor_creator.set_processor(TextDataProcessor())
            processor_creator.process_data(data)
        else:
            print("Failed to find specified article.")
    elif choice == "2":
        music_name = input("Enter music name that you are looking for and to store in database: ")
        music_info = audio_fethcer.search_track(music_name)
        if music_info:
            data = Data("audio", music_info)
            processor_creator.set_processor(AudioDataProcessor())
            processor_creator.process_data(data)
        else:
            print("Couldn't find specified audio.")
    elif choice == "3":
        video_url = input("Enter youtube video link to get info and to store in database: ")
        video_info = video_fetcher.get_video_info(video_url)
        if video_info:
            data = Data("video", video_info)
            processor_creator.set_processor(VideoDataProcessor())
            processor_creator.process_data(data)
        else:
            print("Failed to fetch video information.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
