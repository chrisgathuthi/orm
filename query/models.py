from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class Blog(models.Model):

    """Blog model"""

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = str(timezone.now().date()) + "-" + slugify(self.title)
        return super().save(*args, **kwargs)
