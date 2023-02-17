from django.shortcuts import render
from .models import Video
from django.contrib.postgres.search import SearchQuery, SearchVector


def index(request):
    q = request.GET.get('q') 

    if q:
        vector = SearchVector('title', 'description')
        query = SearchQuery(q)
        videos = Video.objects.annotate(search=vector).filter(search=query)
    else:
        videos = Video.objects.all()

        
    return render(request, 'example/index.html', {'videos' : videos})








