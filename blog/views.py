from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # Fetch posts from the database
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # Render the posts in the template
    return render(request, 'blog/post_list.html', {'posts': posts})
