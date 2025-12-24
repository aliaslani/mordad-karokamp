from ast import AugAssign
from email import message
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.hashers import make_password, check_password


User = get_user_model()

# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(
                request, f"{new_user.username} عزیز، ثبت نام شما با موفقیت انجام شد"
            )
            return redirect("home")
        else:
            print(form.errors)

    return render(request, "accounts/register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        user = authenticate(
            username=data.get("username"), password=data.get("password")
        )
        if user:
            login(request, user)
            messages.success(request, "خوش آمدید")
            return redirect("home")
        else:
            messages.error(request, "کاربری با این مشخصات یافت نشد")
            return render(request, "accounts/login.html", {"form": LoginForm()})


def logout_view(request):
    logout(request)
    messages.success(request, "شما با موفقیت خارج شدید")
    return redirect("login")
