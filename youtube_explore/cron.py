from datetime import datetime
from .models import Video
import requests
from secrets import SECRETS

def my_scheduled_job():
    headers = {
    'Accept': 'application/json',
    }
    params = {
        'key': SECRETS['YOUTUBE_API_KEYS'][0],
        'part': 'snippet',
        'maxResults': 50,
        'order': 'date',
        'type': 'video',
        'publishedAfter': '2020-01-01T00:00:00Z',
        'q': 'education'
    }
    for attempt in range(len(SECRETS['YOUTUBE_API_KEYS'])):
        try:
            response = requests.get('https://youtube.googleapis.com/youtube/v3/search', headers=headers, params=params)
            response_json = response.json()
            print(response_json)
            if ("error" in response_json): raise Exception("unhandlable response")
        except:
            params['key']=SECRETS['YOUTUBE_API_KEYS'][attempt+1]
        else:
            break

    for item in response_json['items']:
        video = Video(
            video_id = item['id']['videoId'], 
            title = item['snippet']['title'],
            description = item['snippet']['description'],
            etag = item['etag'],#signifies change
            channel_id = item['snippet']['channelId'],
            channel_title = item['snippet']['channelTitle'],
            published_at = datetime.strptime(item['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
            thumbnail_url = item['snippet']['thumbnails']['default']['url']
        )
        video.save()
