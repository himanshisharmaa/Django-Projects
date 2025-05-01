from django.shortcuts import render,redirect
from .forms import PostCreateForm,CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required
def post_create(request):
    if request.method=="POST":
        form=PostCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            new_item=form.save(commit=False)
            new_item.user=request.user
            new_item.save()

    else:
        form=PostCreateForm(data=request.GET)
    return render(request,'posts/create.html',{'form':form})
@login_required
def feed(request):
    if request.method=="POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            new_comment.post = post
            new_comment.posted_by = request.user
            new_comment.save()
        else:
            print("Comment errors:", comment_form.errors)
    else:
        comment_form=CommentForm()
    posts=Post.objects.all()
    logged_user=request.user
    return render(request,'posts/feed.html',{'posts':posts,"logged_user":logged_user,'comment_form':comment_form})

def liked_post(request):
    post_id=request.POST.get('post_id')
    print(post_id)
    post=get_object_or_404(Post,id=post_id)
    print(request.user)
    if post.liked_by.filter(id=request.user.id).exists():
        print("Removed")
        post.liked_by.remove(request.user)
    else:
        print("Liked")
        post.liked_by.add(request.user)
    return redirect('/posts/feed')