from django.urls import path
from .views import courses_home

urlpatterns = [
    path('', courses_home, name='courses'),
]
