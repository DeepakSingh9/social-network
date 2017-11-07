# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post,Like
from .forms import PostUploadForm,CommentForm
from django.http import HttpResponse
from django.contrib.auth.models import User



def post_list(request):

    topuser=User.objects.all()[:6]
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts,'topuser':topuser})



def post_detail(request,slug,pk):
    post=get_object_or_404(Post,slug=slug,pk=pk)

    return render(request,'blog/complete_post.html',{'post':post,})


def post_new(request):
    if request.method == "POST":
        form = PostUploadForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug,pk=post.pk)
    else:
        form = PostUploadForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request,slug,pk):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostUploadForm(request.POST,request.FILES,instance=post,)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = request.FILES('file')
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug, pk=post.pk)
    else:
        form = PostUploadForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



def Comment(request,pk):
    if request.method=='POST':
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            commentform.save(commit=False)
            commentform.post=get_object_or_404(Post,pk=pk)
            commentform.save()
            return redirect('blog/post_detail.html',pk=pk)
    else:
        commentform=CommentForm()
    return render(request,'blog/comment.html',{'commentform':commentform})




def profile(request,pk):
    user=get_object_or_404(User,pk=pk)
    alluser=User.objects.all()[:6]
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'blog/profile.html',{'user':user,'posts':posts,'alluser':alluser})







