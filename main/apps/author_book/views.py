from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
from models import *
def index(request):
    response = "Hello, I am your first request!"
    return render(request,"author_book/index.html",response)
# Create your views here.

