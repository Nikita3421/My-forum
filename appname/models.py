from django.db import models

class ArtWork(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(unique=True, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    context = models.TextField(unique=True)
    image_url = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    # author = models.CharField(max_length=200, unique=True)
    context = models.TextField(unique=True)
    emoje = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    

class About(models.Model):    
    context = models.TextField(unique=True)
    image_url = models.URLField()

