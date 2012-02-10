"""
Wrapper for loading templates from the db.
"""
from django.conf import settings
from django.template import TemplateDoesNotExist
from dev-cms.models import Template

def load_template_source(template_name, template_dirs=None):
    try:
        t = Template.objects.get(name=template_name)
        return (t.content, template_name)
    except Template.DoesNotExist:
        error_msg = "Tried %s from db" % template_name
        raise TemplateDoesNotExist, error_msg

load_template_source.is_usable = True
