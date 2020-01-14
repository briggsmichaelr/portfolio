from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 50)
    body = models.CharField(max_length=5000000)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
