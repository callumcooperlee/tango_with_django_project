from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index Page <br><br><a href='http://127.0.0.1:8000/rango/about/'>Go to about page</a>")

def about(request):
    return HttpResponse("About Page <br><br><a href='http://127.0.0.1:8000/rango/'>Go to index page</a>")