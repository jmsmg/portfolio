from django.http import HttpResponse
from django.shortcuts import render
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.

def index(request):
    lottos = GuessNumbers.objects.all()
    sample_sentence = '안녕하세요'
    return render(request, 'lotto/default.html', {
        'lottos':lottos, # context
        })


def hello(request):
    return HttpResponse('<h1 style="color:red">Hello Worlds</h1>')


def post(request):
    form = PostForm()
    return render(request, 'lotto/form.html', {
        'form':form,
        })