from django.contrib import admin
from .models import Account, Blog, Plan
# Register your models here.

admin.site.register(Account)
admin.site.register(Plan)
admin.site.register(Blog)



