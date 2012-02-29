from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse
from devcms.models import Style, Template

def load_css(request, name):
    try:
        s = Style.objects.get(name=name+'.css')
    except Style.DoesNotExist:
        try:
            s = Style.objects.get(name=name)
        except Style.DoesNotExist:
            raise Http404

    return HttpResponse(s.content, mimetype="text/css")

def direct_to_cms(request, path):
    if path == "":
        path = "/"
    else:
        if path[0] <> "/":
            path = "/" + path
        if path[-1] <> "/":
            path = path + "/"

    try:
        t = Template.objects.get(path=path)
    except Page.DoesNotExist:
        raise Http404
    
    return render_to_response(t, context_instance=RequestContext(request))
