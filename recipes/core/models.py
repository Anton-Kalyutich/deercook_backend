from django.db import models

# Create your models here.
class Recipe(models.Model): 
    dish_name = models.CharField(max_length=30) 
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='local_images/', default="local_images/default.jpg")

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50000)
