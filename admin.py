from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from devcms.models import Template, Style

class TemplateAdmin(MPTTModelAdmin):
    pass

admin.site.register(Template, TemplateAdmin)

class StyleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Style, StyleAdmin)

