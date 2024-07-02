from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def appHello(request):
    return HttpResponse('Hello from app')