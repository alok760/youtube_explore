from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
import requests

def index(request):
    headers = {
    'Accept': 'application/json',
    }
    params = {
        'key': 'AIzaSyDHEKkOM6E4x_91sOTx-MFeGP2fYLR7i-I',
        'part': 'snippet',
        'maxResults': 5,
        'order': 'date',
        'type': 'video',
        'publishedAfter': '2020-01-01T00:00:00Z',
        'q': 'education'
    }
    response = requests.get('https://youtube.googleapis.com/youtube/v3/search', headers=headers, params=params)
    response_json = response.json()
    from .response import response_json
    for item in response_json['items']:
        video = Video(
            video_id = item['id']['videoId'], 
            title = item['snippet']['title'],
            description = item['snippet']['description'],
            etag = item['etag'],#signifies change
            channel_id = item['snippet']['channelId'],
            channel_title = item['snippet']['channelTitle'],
            # publishedAt = 
            # thumbnail_url = 
        )
        video.save()
    return HttpResponse("Hello, World!")

def search(request):
    pass
# Create your views here.
