from django.shortcuts import render
from core.models import Post, User


def jadid(request):
    p = Post.objects.all()
    return render(request, "core/home.html", context={"posts": p})


def user_list(request):
    u = User.objects.all()
    return render(request, "core/users.html", {"users": u})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "core/post_detail.html", context={"post": post})


def new_post(request):
    return render(request, "core/new_post.html")
