
from data_processing.creator import DataProcessorCreator
from data_processing.processors.audio_processor import AudioDataProcessor
from data_processing.processors.text_processor import TextDataProcessor
from data_processing.processors.video_processor import VideoDataProcessor
from data_processing.data import Data
from data_processing.fetchers.audio_fetcher import AudioFetcher
from config.config import spotify_client_id, spotify_client_secret


def main():
    
    audio_fethcer = AudioFetcher(spotify_client_id, spotify_client_secret)
    processor_creator = DataProcessorCreator()


    print("Choose data type to process:")
    print("1. Text")
    print("2. Audio")
    print("3. Video")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        text_data = input("Enter the text you want to process: ")
        data = Data("text", text_data)
        processor_creator.set_processor(TextDataProcessor())
        processor_creator.process_data(data)
    elif choice == "2":
        query_field = input("Enter music name that you are looking for and to store in database: ")
        audio_data = audio_fethcer.search_track(query_field)
        if audio_data is not None:
            data = Data("audio", audio_data)
            processor_creator.set_processor(AudioDataProcessor())
            processor_creator.process_data(data)
        else:
            print("Couldn't find specified audio.")
    elif choice == "3":
        video_data = {
            "name": "Video Name",
            "artists": ["Artist 1", "Artist 2"],
            "album": "Album Name",
            "preview_url": "http://example.com/video.mp4"
        }
        data = Data("video", video_data)
        processor_creator.set_processor(VideoDataProcessor())
        processor_creator.process_data(data)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
