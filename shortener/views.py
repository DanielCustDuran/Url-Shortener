from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import get_object_or_404

from django.views import View

from django.http import HttpResponse, HttpResponseRedirect

from .forms import SubmitUrlForm
from .models import URL

# Create your views here
class HomeView(View):
    """docstring for HomeView."""
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "form": the_form
        }
        return render(request, "shortener/Home.html", context)

    def post(self, request, *args, **kwargs ):
        form = SubmitUrlForm(request.POST)
        context = {"form" : form}
        template = "shortener/Home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = URL.objects.get_or_create(url = new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already.html"
        return render(request, template, context)

class URLRedirectView(View):
    def get(self, request, shortcode = None, *args, **kwargs):
        obj = get_object_or_404(URL, shortcode = shortcode)
        return HttpResponseRedirect(obj.url)
