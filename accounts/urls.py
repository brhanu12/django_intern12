from django.urls import path
from django.http import HttpResponse
from . import views


def test_profile(request):
    return HttpResponse("PROFILE URL IS WORKING")


urlpatterns = [

    path(
        "register/",
        views.register,
        name="register",
    ),

    path(
        "login/",
        views.user_login,
        name="login",
    ),

    path(
        "logout/",
        views.user_logout,
        name="logout",
    ),

    path(
        "profile/",
        test_profile,
        name="profile",
    ),

]