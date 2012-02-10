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

class Page(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    path = models.CharField(max_length=255, db_index=True, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    template = models.ForeignKey('Template')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('path', 'name',)
        
    class MPTTMeta:
        order_insertion_by = ['name']
       
class Content(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    page = models.ForeignKey('Page')
    var_name = models.CharField(max_length=255, db_index=True)
    content = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
