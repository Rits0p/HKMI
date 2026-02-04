from django.urls import path
from .views import courses_home

urlpatterns = [
    path('home/', courses_home, name='courses_home'),
]
