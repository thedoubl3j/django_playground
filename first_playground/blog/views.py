from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about_page(request):
    return HttpResponse('<h1>About this Blog</h1>')
