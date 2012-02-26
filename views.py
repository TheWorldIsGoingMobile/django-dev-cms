from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse
from devcms.models import Style

def load_css(request, name):
    try:
        #s = Style.objects.get(name=name+'.css')
        s = Style.objects.get(name=name)
        return HttpResponse(s.content, mimetype="text/css")
    except Style.DoesNotExist:
        raise Http404
