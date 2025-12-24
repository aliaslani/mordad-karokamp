from django.shortcuts import redirect, render, get_object_or_404
from core.models import Post, Like
from core.forms import PostForm, EditPostForm
from django.contrib import messages
import shutil
import pathlib
from accounts.models import User
from django.contrib.auth.decorators import login_required


def jadid(request):
    p = Post.objects.filter(is_deleted=False)
    return render(request, "core/home.html", context={"posts": p})


def user_list(request):
    u = User.objects.all()
    return render(request, "core/users.html", {"users": u})


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "core/post_detail.html", context={"post": post})


# def new_post(request):
#     if request.method == "POST":
#         form_data = request.POST
#         t = form_data.get("title")
#         content = form_data.get("content")
#         username = form_data.get("user")
#         category = form_data.get("category")
#         user = User.objects.filter(username=username).first()
#         if user:
#             Post.objects.create(title=t, content=content, user=user, category=category)
#         else:
#             print("User is not defined")
#     return render(request, "core/new_post.html")


@login_required
def new_post(request):
    # if request.user.is_authenticated:
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, "پست شما با موفقیت ثبت شد")
            return redirect("home")

    return render(request, "core/new_post.html", {"harchi": form})
    # else:
    #     messages.error(request, "برای دیدن محتوای این صفحه باید ابتدا لاگین کنید")
    #     return redirect("login")


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user == request.user:
        post.is_deleted = True

        post.save()
        address = pathlib.Path(post.image.url)
        shutil.rmtree(address)
        messages.success(request, "پست مورد نظر با موفقیت پاک شد")
        return redirect("home")
    else:
        return redirect("post_detail", post_id=post.id)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = EditPostForm(instance=post)

    user = post.user
    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(commit=False)
            post.user = user
            post.save()

            messages.success(request, "تغییرات با موفقیت اعمال شد")
            return redirect("post_detail", post_id=post.id)
    return render(request, "core/edit_post.html", {"form": form, "post": post})


def like(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        like = Like.objects.create(user=request.user, post=post)
        return redirect("post_detail", post_id=post.id)
