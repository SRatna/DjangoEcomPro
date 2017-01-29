from __future__ import unicode_literals

from django.db import models

# Create your models here.

class profiles(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='description text')

    def __unicode__(self):
        return self.name
