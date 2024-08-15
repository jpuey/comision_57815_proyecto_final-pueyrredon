from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login_request, name= "Login"),
    path('register/', register, name='Register'),
    path('logout', LogoutView.as_view(template_name='centromed/index.html'), name="Logout"),

    ]
