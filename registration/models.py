# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], blank=True, max_length=128)
    profile_image = models.ImageField(upload_to='profilepic/', blank=True)
    organisation = models.CharField(max_length=100,blank=True,null=True)
    designation = models.CharField(max_length=50,blank=True,null=True)
    followed_by = models.ManyToManyField('self', related_name='follows', symmetrical=False)



    def __str__(self):
        return self.user.username




