# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Template(MPTTModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    tree_name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    content = models.TextField(blank=True)
    path = models.CharField(max_length=255, null=True, blank=True, db_index=True, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    class MPTTMeta:
        order_insertion_by = ['tree_name']

class Style(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

