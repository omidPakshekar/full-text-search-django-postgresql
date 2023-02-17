from django.contrib import admin
from django.urls import path

from example import views as example_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', example_views.index),
    
]
