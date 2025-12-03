from django.shortcuts import redirect, render
from core.models import Post, User
from core.forms import PostForm


def jadid(request):
    p = Post.objects.all()
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
def new_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.pop("username")
            user = User.objects.filter(username=username).first()
            if user:
                new_post = Post.objects.create(**data, user=user)
                print(new_post.id)
                return redirect("home")

    return render(request, "core/new_post.html", {"harchi": form})
