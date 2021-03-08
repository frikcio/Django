from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    book = models.CharField(max_length=120)
    author = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.book


class BookTable(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, unique=True)
    holder = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'a book "{self.book}" is already has been got by {self.holder}'


class Grant(models.Model):
    grant = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.grant


class SomeUser(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    holder = models.ForeignKey(SomeUser, on_delete=models.DO_NOTHING)
    topic = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"post {self.topic}"


class Comment(models.Model):
    user_name = models.ForeignKey(SomeUser, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    like = models.ForeignKey(Grant, on_delete=models.DO_NOTHING, default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'user {self.user_name} left comment "{self.comment}" to {self.post}'
