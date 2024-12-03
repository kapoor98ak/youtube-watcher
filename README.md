# YouTube Comment Monitoring and Alerts System

## Overview
Hi, I have made this project to tackle a problem that I regularly faced. I have videos that I was a co-author of, and these videos were not uploaded on my channel. So, when these videos got some comments that I could answer to, I did not have any way of doing it. Hence, I created this end-to-end realtime data pipeline in Kafka and Python.

This project builds a Python program that monitors specific YouTube videos in a playlist for updates(likes, views, and comments), streams data into Kafka (Confluent Cloud Kafka), and processes it to generate alerts. 

This data pipeline tracks changes such as new comments, views, likes, and replies, and sends notifications or alerts via Telegram.

## Features
- Monitors a playlist of YouTube videos for:
  - New comments.
  - Changes in views, likes, and other statistics.
- Uses Kafka to stream video and comment data.
- Processes changes in real-time with ksqlDB.
- Sends alerts for specific changes (e.g., a comment mentioning you) to a Telegram bot.

## System Architecture

![YouTube Comment Monitoring Architecture](https://github.com/user-attachments/assets/e620163d-0bf3-422b-b9bd-16472a67a1b3)




## Prerequisites
- Python 3.8+
- A YouTube Data API Key.
- A Kafka cluster (e.g., Confluent Cloud).
- A Telegram account and bot token.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/youtube-alert-system.git
   cd youtube-alert-system
   ```
2. **Set Up Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate
    ```
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Create CONFIG file**
    ```bash
    config = {
    "google_api_key": "...",
    "youtube_playlist_id": "...",
    "topic": "youtube_videos",
    "kafka": {
        "bootstrap.servers": "...",
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': "...",
        'sasl.password': "...",
    },
    "schema_registry": {
        "url": "...",
        "basic.auth.user.info": "<username>:<password>"
    },
    "OPENAI_API_KEY": "..."
    }
    ```
5. **Run the Script**
    ```bash
    ./youtube-watcher.py
    ```

## Usage
1. Modify Playlist: Add videos to the playlist to automatically start monitoring them.
2. Telegram Alerts: Receive real-time updates when monitored statistics change.


## Tools and Technologies
* Python: Core scripting language.
* YouTube Data API: To fetch video and comment data.
* Kafka: For streaming and processing events.
* ksqlDB: For detecting changes in streaming data.
* S3: For storage of historical data, new comments.
* SNS: For alerting the user and triggering the lambda.
* Lambda: For comment processing and parsing for content.
* Telegram: For alert notifications.

## License

```
MIT License
```