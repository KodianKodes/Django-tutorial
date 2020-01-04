from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home page")

def news(request):
    return HttpResponse('the news page')

def contact(request):
    return HttpResponse('contact us page')


def about(request):
    return HttpResponse('about us page')

