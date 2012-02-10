from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse
from dev-cms.models import Style, Page

def load_css(request, name):
    try:
        #s = Style.objects.get(name=name+'.css')
        s = Style.objects.get(name=name)
        return HttpResponse(s.content, mimetype="text/css")
    except Style.DoesNotExist:
        raise Http404
    
def direct_to_cms(request, path):
    if path == "":
        path = "/"
    else:
        if path[0] <> "/":
            path = "/" + path
        if path[-1] <> "/":
            path = path + "/"

    try:
        p = Page.objects.get(path=path)
        d = {}
        for c in p.content_set.all():
            d[c.var_name] = c.content
        return render_to_response(p.template, d, context_instance=RequestContext(request))
    except Page.DoesNotExist:
        raise Http404
