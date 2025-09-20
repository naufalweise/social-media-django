from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# all post list, homepage
def all_post_list(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(request, "posts/all-post-list.html", {'posts': posts, 'post_form': form})

def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect('/posts/')
    
    # TODO: add error handling
    return redirect('/posts')