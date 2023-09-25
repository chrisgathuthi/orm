from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Blog, User
from .forms import RegistrationForm, LoginForm

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(self.request, "index.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(self.request.POST or None)

        if form.is_valid():
            form.save()
            return redirect("login")
        return render(self.request, "index.html", {"form": form})


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(self.request, "login.html", {"form": form})


class BlogView(View):

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        return render(self.request, "home.html", {"blogs": blogs})


class UsernameValidation(View):

    def post(self, request, *args, **kwargs):
        if User.objects.filter(username=self.request.POST["username"]).exists():
            return HttpResponse(" <p class='errors' id='usernameError'>The username already exists</p> \
                <button type='button' class='btn btn-secondary' id='submitBtn' disable='disable'> submit</button> ")
        else:
            return HttpResponse("<p class='errors' id='usernameError'></p> \
                 <button type='submit' class='btn btn-primary' id='submitBtn' > submit</button> ")


class EmailValidation(View):

    def post(self, request, *args, **kwargs):
        if User.objects.filter(email=self.request.POST["email"]).exists():
            return HttpResponse(" <p class='errors' id='emailError'>The email already exists</p> \
                <button type='submit' class='btn btn-secondary' id='submitBtn'  disable='disable'> submit</button>")
        else:
            return HttpResponse("<p class='errors' id='emailError'></p> \
                <button type='submit' class='btn btn-primary' id='submitBtn'> submit</button> ")
