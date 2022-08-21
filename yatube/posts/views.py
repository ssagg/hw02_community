from django.shortcuts import render, get_object_or_404
from .models import Group, Post

# Create your views here.

# Главная страница
POSTS_NUM = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:POSTS_NUM]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:POSTS_NUM]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
