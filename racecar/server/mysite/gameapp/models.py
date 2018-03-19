# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class identities(models.Model):
    id = models.AutoField(primary_key=True)
    mac = models.CharField(max_length = 20)
    ips = models.CharField(max_length = 20)
    opsys = models.CharField(max_length = 20)
    #username = models.CharField(max_length = 255)
    
