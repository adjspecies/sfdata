from django.db import models


class Tag(models.Model):

    name = models.TextField()


class Author(models.Model):

    name = models.TextField()


class Post(models.Model):

    story_id = models.IntegerField()
    title = models.TextField()
    date = models.DateTimeField()
    wordcount = models.IntegerField()
    in_series = models.BooleanField()
    views = models.IntegerField()
    faves = models.IntegerField()
    comments = models.IntegerField()
    votes = models.IntegerField()
    score = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
