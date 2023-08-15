from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Plan(models.Model):

    """user plan subscriptions"""
    class Packages(models.TextChoices):
        NOVICE = "novice", "Novice"
        ELITE = "elite", "Elite"  # lowercase, check celery task
    package = models.CharField(verbose_name="plan", max_length=10, choices=Packages.choices,
                               default=None)  # Novice, Elite, Legendary
    level = models.PositiveIntegerField(default=1)
    link = models.URLField(verbose_name="link", unique=True, editable=False, null=True)
    commission = models.DecimalField(decimal_places=2, max_digits=10, editable=False, default=0.00)
    referals = models.ManyToManyField("Account", related_name="invites")
    is_paid = models.BooleanField(verbose_name="account validity", default=True, blank=True) 

    def __str__(self):
        return self.package

class Account(models.Model):

    """Registered user accounts"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    plan = models.ManyToManyField(Plan, related_name="subscription", blank=True)

    def __str__(self):
        return f"{self.user.username}'s account"

class Blog(models.Model):

    """Blog model"""

    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

