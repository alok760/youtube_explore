from django.http.response import HttpResponseNotModified
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Video
from django.core import serializers
from datetime import datetime
from .documents import VideoDocument

def index(request):
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

