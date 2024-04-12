# Real-Time Data Processing System

A real-time data processing system that receives data from multiple sources, processes it in real-time, and stores it in a database. The system supports different types of data, such as text, audio, and video, and processes them accordingly.

## Overview

This project implements a real-time data processing system using the Factory Method design pattern. It includes modules for processing different types of data, such as text, audio, and video. The system fetches data from various sources, processes it in real-time using specialized processing modules, and stores it in a database for future use.

## Components

1. **Data Processing Modules**: Modules for processing different types of data, such as text, audio, and video.
2. **Data Storage**: Database for storing processed data.
3. **Data Fetchers**: Components for fetching data from various APIs, such as Spotify, IEEE Xplore, and Youtube DATA API.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Tikava/css-217.git
   ```

2. Install dependencies:

   ```bash
   cd css-217/assignment-5/ex-2
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root directory and add your environment variables:

   ```plaintext
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   YOUTUBE_DATA_API_KEY=your_google_api_key
   IEEE_XPLORE_API_KEY=your_ieee_xplore_api_key
   ```

## Usage

1. Run the main script:
   ```python
   python main.py
   ```

2. Follow the prompts to choose the data type to process and provide any necessary input.