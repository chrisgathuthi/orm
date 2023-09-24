from django.urls import path
from .views import HomeView, SignInView, BlogView, UsernameValidation, EmailValidation

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("login/", SignInView.as_view(), name="login"),
    path("home/", BlogView.as_view(), name="blog"),
    path("username-validation/", UsernameValidation.as_view(),name="username-validation"),
    path("email-validation/", EmailValidation.as_view(), name="email-validation"),
]