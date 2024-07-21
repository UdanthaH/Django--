from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    # Fetch posts from the database
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # Render the posts in the template
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # Fetch the post by primary key or return 404 if not found
    post = get_object_or_404(Post, pk=pk)
    
    # Render the post in the template
    return render(request, 'blog/post_detail.html', {'post': post})
