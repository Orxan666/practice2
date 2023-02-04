from django.shortcuts import render

# Create your views here.

from .models import Article


def blog_list(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', context={'articles': articles})


def blog_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article.html', context={'article': article})
