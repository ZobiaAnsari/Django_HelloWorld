from django.http import HttpResponse
def hello(resource):
    return HttpResponse("Hello World")