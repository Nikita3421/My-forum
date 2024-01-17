from django.contrib import admin
from .models import Post, ArtWork, Comment, About

admin.site.register(Post)
admin.site.register(ArtWork)
admin.site.register(Comment)
admin.site.register(About)

# Register your models here.
