from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from devcms.models import Template, Style

class TemplateAdmin(MPTTModelAdmin):
    #pass
    list_display = ('tree_name', 'name', 'path',)

admin.site.register(Template, TemplateAdmin)

class StyleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Style, StyleAdmin)

