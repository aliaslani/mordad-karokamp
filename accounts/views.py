from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib import messages
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

    return render(request, "accounts/register.html", {"form": form})
