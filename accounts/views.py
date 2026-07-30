from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)
            messages.success(
    request,
    "Registration successful! Welcome."
)

            return redirect("blog_list")
        else:
         print(form.errors)   # change this to your blog list URL name

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )
def user_login(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)
            messages.success(
    request,
    "Welcome back!"
)

            return redirect("blog_list")   
        

    else:

        form = AuthenticationForm()

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )

@login_required
def user_logout(request):

    logout(request)

    messages.success(
    request,
    "You have been logged out successfully."
)

    return redirect("login")
@login_required

def profile(request):

    return render(

        request,

        "accounts/profile.html",

        {

            "profile": request.user.profile

        }

    )