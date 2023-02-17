from django.shortcuts import render
from .models import Video


def index(request):
    q = request.GET.get('q') 

    videos = Video.objects.all()
    if q:
        videos = Video.objects.filter(title_search=q)
        
    return render(request, 'example/index.html', {'videos' : videos})








