from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from dev-cms.models import Template, Style, Page, Content

class TemplateAdmin(MPTTModelAdmin):
    pass

admin.site.register(Template, TemplateAdmin)

class StyleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Style, StyleAdmin)

class PageAdmin(MPTTModelAdmin):
    pass

admin.site.register(Page, PageAdmin)

class ContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Content, ContentAdmin)
