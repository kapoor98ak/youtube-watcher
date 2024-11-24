#!/usr/bin/env python
import json
import logging
import sys
from pprint import pformat

import requests
from config import config


# import pretty_errors
# pretty_errors.configure(
#     separator_character='*',  # Character used for separators
#     filename_display=pretty_errors.FILENAME_EXTENDED,  # Show full file paths
#     line_number_color='red',  # Color for line numbers
#     code_color='cyan',        # Color for source code
#     line_color='bright_white',# Color for separator lines
#     display_link=True         # Add clickable links in supported terminals
# )


def fetch_youtube_playlist_page(google_api_key, youtube_playlist_id, page_token=None):
    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems",
                            params={
                                'key': google_api_key,
                                'playlistId': youtube_playlist_id,
                                'part': 'contentDetails, status',
                                'pageToken': page_token,
                            })
    payload = json.loads(response.text)
    # logging.debug("Got %s", payload)
    return payload


def fetch_playlist_items(google_api_key, youtube_playlist_id, page_token=None):
    payload = fetch_youtube_playlist_page(google_api_key, youtube_playlist_id, page_token)

    # Serve up the items on that page - now, the Python generator comes in.
    yield from payload['items']

    # If I give [nextPageToken] then on the last page, it does not produce on results.
    next_page_token = payload.get('nextPageToken')
    if next_page_token:
        yield from fetch_playlist_items(google_api_key, youtube_playlist_id, next_page_token)


def fetch_youtube_video_page(google_api_key, video_id, page_token=None):
    response = requests.get("https://www.googleapis.com/youtube/v3/videos",
                            params={
                                'key': google_api_key,
                                'id': video_id,
                                'part': 'snippet, statistics',
                                'pageToken': page_token,
                            })
    payload = json.loads(response.text)
    return payload


def fetch_videos(google_api_key, video_id, page_token=None):
    payload = fetch_youtube_video_page(google_api_key, video_id, page_token)
    # logging.info(pformat(payload))

    yield from payload['items']

    # If I give [nextPageToken] then on the last page, it does not produce on results.
    next_page_token = payload.get('nextPageToken')
    if next_page_token:
        yield from fetch_youtube_video_page(google_api_key, video_id, next_page_token)


def summarize(video):
    return {
        "video_id": video['id'],
        "title": video['snippet'].get('title'),
        "channel": video['snippet'].get('channelTitle', 0),
        "views": int(video['statistics'].get('viewCount', 0)),
        "likes": video['statistics']['likeCount'],
        "comments": video['statistics']['commentCount'],
    }


def main():
    logging.info("START")
    google_api_key = config['google_api_key']
    youtube_playlist_id = config['youtube_playlist_id']

    for video_items in fetch_playlist_items(google_api_key, youtube_playlist_id):
        video_id = video_items['contentDetails'].get('videoId')
        for video in fetch_videos(google_api_key, video_id):
            logging.info("Video information: %s", pformat(summarize(video)))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())
