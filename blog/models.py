from django.db import models

# Create your models here.


class Author (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    updated = models.DateField(auto_now_add=True)
    content=models.TextField()
    created = models.DateField(auto_now=True)
    def __str__(self):
        return self.title
