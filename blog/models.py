from django.db import models

# Create your models here.
class Post(models.Model):
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=150)
    text=models.TextField()
    time_created=models.DateTimeField(auto_now_add=True ,auto_now=False)
    time_publish=models.DateTimeField(auto_now_add=False ,auto_now=True)


    def __str__(self):
        return self.title
