from django.shortcuts import render
from django.views import View
from .models import Blog, Account, User

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.prefetch_related("blog_set")
        print(accounts)
        return render(self.request,"queries.html",{"blogs":Blog.objects.select_related("account__user")})