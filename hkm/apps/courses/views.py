from django.shortcuts import render

# Create your views here.
def courses_home(request):
    return render(request, 'pages/course.html')