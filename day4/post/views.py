from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html', {'posts':posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    categories = Category.objects.all()
    return render(request, 'post/detail.html', {'post':post, 'categories':categories})