from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404

from .models import URL

# Create your views here.

def redirect_view(request, shortcode = None, *args, **kwargs):
    obj = get_object_or_404(URL, shortcode=shortcode)
    return HttpResponse("Hello {sc}".format(sc = obj.url))

class RedirectView(View):
    def get(self, request, shortcode = None, *args, **kwargs):
        obj = get_object_or_404(URL, shortcode = shortcode)
        return HttpResponse("Hello {sc} again".format(sc = obj.url))
