from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello Worlds</h1>')
    # return render('templates/index.html', {

    # })

def hello(request):
    return HttpResponse('<h1 style="color:red">Hello Worlds</h1>')
