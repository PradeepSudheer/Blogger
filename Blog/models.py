from django.db import models

# Create your models here.
class Blogpost(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=4000)

    def __str__(self):
        return self.title