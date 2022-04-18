from django.shortcuts import render
from .models import Post
# Create your views here.

def post_index(request):
    post = Post.objects.all().order_by()
    context = {'post': post}
    return render(request, 'blog/post_index.html', context)