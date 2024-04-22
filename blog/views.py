from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.


#this adds a post list function the defers to the post list html page. We respond to a request, send the browser to the associated html page, and pass any date on to it
def post_list(request):
    #this is where you are going to put your queries (for the most part)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})