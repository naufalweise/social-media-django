from django.shortcuts import render, redirect
from .models import Post, PostMedia
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# all post list, homepage
@login_required
def all_post_list(request):
    posts = Post.objects.prefetch_related('postmedia_set').all()
    form = PostForm()
    return render(request, "posts/all-post-list.html", {'posts': posts, 'post_form': form})

@login_required
@require_POST
def create_post(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        media_files = form.cleaned_data["media_files"]
        for f in media_files:
            PostMedia.objects.create(post=new_post, file=f)
        return redirect('/posts/')
    
    # TODO: add error handling
    return redirect('/posts')