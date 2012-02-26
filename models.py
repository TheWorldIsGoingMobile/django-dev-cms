# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Template(MPTTModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    class MPTTMeta:
        order_insertion_by = ['name']

class Style(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

