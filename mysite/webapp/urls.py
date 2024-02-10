# webapp/urls.py
from django.urls import path
from .views import home, process_images_view

urlpatterns = [
    path('', home, name='home'),
    path('', process_images_view, name='process_images'),
]
