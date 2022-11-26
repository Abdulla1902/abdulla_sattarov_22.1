from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
date = datetime.now().date()

def main(request):
    return HttpResponse('<h2><center>Главная<center><h2>')

def hello(request):
    return HttpResponse('<h2><center>Hello! Its my project<center><h2>')

def date_now(request):
    return HttpResponse(f'<h2><center>{date}<center><h2>')

def goodbye(request):
    return HttpResponse('<h2><center>Goodbye user!<center><h2>')