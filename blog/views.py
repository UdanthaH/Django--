from django.shortcuts import render
from .models import Post  # Import your Post model

def post_list(request):
    posts = Post.objects.all()  # Query your Post objects
    return render(request, 'blog/post_list.html', {'posts': posts})
