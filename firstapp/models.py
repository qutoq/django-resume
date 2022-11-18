from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Post(models.Model):  #¯\_( ͡❛ ͜ʖ ͡❛)_/¯
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(default='', max_length=20)
    image = models.ImageField(upload_to='block/', blank=True, null=True)
    text = models.TextField(default='')
    link = models.CharField(default='', max_length=50)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    company = models.CharField(max_length=50, default='')
    message = models.TextField(max_length=1000, default='')
    timeAdd = models.DateTimeField(auto_now_add=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        if not self.read:
            return 'Новое сообщение от: ' + str(self.name)
        return str(self.name) + ' | ' + str(self.message)

