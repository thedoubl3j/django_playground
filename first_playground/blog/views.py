from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')

def about_page(request):
    return render(request, 'blog/about.html')
    #you got to minute 8;45 in the video
