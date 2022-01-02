from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Video
from django.core import serializers
from datetime import datetime
from .documents import VideoDocument
import requests

def index(request):
    headers = {
    'Accept': 'application/json',
    }
    params = {
        'key': 'AIzaSyDHEKkOM6E4x_91sOTx-MFeGP2fYLR7i-I',
        'part': 'snippet',
        'maxResults': 50,
        'order': 'date',
        'type': 'video',
        'publishedAfter': '2020-01-01T00:00:00Z',
        'q': 'education'
    }
    response = requests.get('https://youtube.googleapis.com/youtube/v3/search', headers=headers, params=params)
    response_json = response.json()
    # from .response import response_json
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
    return HttpResponse("Hello, World!")



def get(request):
    page = int(request.GET['page'])
    page_size = int(request.GET['page_size'])
    OFFSET = page_size * (page - 1)
    LIMIT = page_size
    query = Video.objects.all()[OFFSET:OFFSET+LIMIT]
    response_data = serializers.serialize('json', query)
    return HttpResponse(response_data, content_type='application/json')

def search(request):
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 20))
    search_phrase = request.GET.get('search', None)
    if search_phrase:
        sl = VideoDocument.search().query("multi_match", query=search_phrase, fields=['title','description'])
        query = sl.to_queryset()
    else:
        query = Video.objects.all()
    sort = request.GET.get('sort', 'desc')
    sort_attr = '-published_at' if sort=='desc' else 'published_at'
    query = query.order_by(sort_attr) 
    OFFSET = page_size * (page - 1)
    LIMIT = page_size
    query = query[OFFSET:OFFSET+LIMIT]
    response_data = serializers.serialize('json', query)
    return HttpResponse(response_data, content_type='application/json')

# Create your views here.
