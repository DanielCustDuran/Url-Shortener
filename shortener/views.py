from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404

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
        if form.is_valid():
            print(form.cleaned_data.get("url"))
        context = {"form" : form}
        return render(request, "shortener/Home.html", context)

class RedirectView(View):
    def get(self, request, shortcode = None, *args, **kwargs):
        obj = get_object_or_404(URL, shortcode = shortcode)
        return HttpResponseRedirect(obj.url)
