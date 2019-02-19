from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 30)
    issue_date = models.DateTimeField(default=timezone.now)
    #Scholar_name = models.ForeignKey(User, on_delete=models.CASCADE)
    ISBN = models.IntegerField(default = 4546378982176)
    genre=models.CharField(max_length=30)


    def __str__(self):
        return self.title