from django.shortcuts import render
from .models import Post

# all post list, homepage
def all_post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/all-post-list.html", {'posts': posts})

def create_post(request):
    pass
    #return render(request, "post")