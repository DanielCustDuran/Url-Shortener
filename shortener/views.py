from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404

from .models import URL

# Create your views here.
def test_view(request):
    return HttpResponse("Some foo")
    
def redirect_view(request, shortcode = None, *args, **kwargs):
    obj = get_object_or_404(URL, shortcode=shortcode)
    print(obj.url)
    return HttpResponseRedirect(obj.url)

class RedirectView(View):
    def get(self, request, shortcode = None, *args, **kwargs):
        obj = get_object_or_404(URL, shortcode = shortcode)
        return HttpResponseRedirect(obj.url)
