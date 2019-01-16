# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category, null=True, related_name="blog_post", on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title
