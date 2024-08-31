# resizer/urls.py

from django.urls import path
from .views import resize_image_view, success_view

urlpatterns = [
    path('', resize_image_view, name='resize_image'),
    path('success/', success_view, name='success'),
]
