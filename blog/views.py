from django.shortcuts import render
from .models import Post
# Create your views here.

def blog_index(request):
    post = Post.objects.all().order_by('-created_at')
    context = {'post': post}
    return render(request, 'blog/post_index.html', context)
    