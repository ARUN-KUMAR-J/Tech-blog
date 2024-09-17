from typing import Iterable
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Posts (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url=models.URLField(null=True)
    created= models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

class aboutus(models.Model):
    content=models.TextField()
    Programming_Languages=models.TextField()
    Database_Management=models.TextField()
    Web_development=models.TextField()
    problem_solving=models.TextField()
    
    
class example(models.Model):
    content=models.TextField()
    new_id=models.IntegerField()