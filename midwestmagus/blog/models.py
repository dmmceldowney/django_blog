from django.db import models
from ckeditor.fields import RichTextField

import datetime as dt


class Tag(models.Model):
    text = models.CharField(max_length=50, null=False, unique=True)

    class Meta:
        ordering = ('text',)

    def __str__(self):
        return self.text


class Post(models.Model):
    title = models.CharField(max_length=200, null=False, unique=True)
    blurb = models.CharField(max_length=200, null=False)
    body = RichTextField()
    publish_date = models.DateTimeField(null=False, auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return f"{self.pk}-{self.title}"
