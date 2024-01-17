from django.shortcuts import render
from .models import Post, Comment, About, ArtWork
from django.shortcuts import render, get_object_or_404

def post_list(request):
    # Получите все посты и работы искусства из базы данных
    posts = Post.objects.all()
    artworks = ArtWork.objects.all()

    # Передайте их в контекст и отрендерьте шаблон
    return render(request, 'project/post_list.html', {'posts': posts, 'artworks': artworks})

def post_view(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.all()
    return render(request, 'project/post_view.html', {'post': post,"comments": comments})


def artwork_list(request):
    artworks = ArtWork.objects.all()
    return render(request, 'project/post_list.html', {'artworks': artworks})

def artwork_view(request, pk):
    artwork = ArtWork.objects.get(pk=pk)
    comments = Comment.objects.all()
    return render(request, 'project/artwork_view.html', {'artwork': artwork,"comments": comments})

def About_info(request):
    about= About.objects.all()
    return render(request, 'project/about.html', {'about': about})


