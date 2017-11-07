# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from tinymce.widgets import TinyMCE
from tinymce import models as t_m
from django.template.defaultfilters import slugify
from django.apps import AppConfig



class Category(models.Model):
    category_name=models.CharField(max_length=128)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural='Categories'




class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = t_m.HTMLField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image=models.FileField(blank=True,upload_to='blogimages/pic')
    category=models.ForeignKey(Category,blank=True,null=True)
    slug=models.SlugField(null=True,blank=True,max_length=500)









    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)




    def publish(self):
        self.published_date = timezone.now()
        self.save()





    def __str__(self):
        return self.title



class Like(models.Model):
    post=models.ForeignKey(Post)
    user=models.ForeignKey(User)
    created=models.DateTimeField(auto_now_add=True)




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)







class SmallPost(models.Model):
    writer=models.ForeignKey(User)
    text=models.TextField(max_length=150)
    created_date=models.DateTimeField(auto_now_add=True)











