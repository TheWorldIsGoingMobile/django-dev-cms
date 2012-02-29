"""
In your template you should use the following:

{% load devcms_tags %}
"""
from django import template
from django.contrib.markup.templatetags.markup import textile, markdown, restructuredtext
from django.utils.safestring import mark_safe

register = template.Library()

def process_markup(text, markup):
    if markup == 'textile':
        return textile(text)
    elif markup == 'html':
        return mark_safe(text)
    elif markup == 'markdown':
        return markdown(text)
    elif markup == 'rst':
        return restructuredtext(text)
    else:
        return mark_safe('<pre>' + text + '</pre>')

class MarkupNode(template.Node):
    def __init__(self, nodelist, markup):
        self.nodelist = nodelist
        self.markup = markup

    def render(self, context):
        rendered = self.nodelist.render(context)
        return process_markup(rendered, self.markup)

@register.tag('markup')
def do_markup(parser, token):
    """
    Delimiter markup text to be converted to HTML.

    Usage:

    {% markup textile|markdown|restructuredtext %}
    h1. This is a header in textile

    !/static/img/mypicture.jpg!

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam varius est at
    purus eleifend commodo. Quisque et orci id est interdum viverra. Ut lacinia
    nunc elit. Integer gravida quam tellus, in sollicitudin ligula.
    {% endmarkup %}
    """
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, markup = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])

    if not (markup in ('textile', 'markdown', 'restructuredtext')):
        raise template.TemplateSyntaxError("%r tag's argument should be textile or markdown or restructuredtext" % tag_name)

    nodelist = parser.parse(('endmarkup',))
    parser.delete_first_token()

    return MarkupNode(nodelist, markup)

