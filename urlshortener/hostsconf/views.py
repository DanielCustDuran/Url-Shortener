from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDIRECT_PATH = getattr(settings, "DEFAULT_REDIRECT_PATH", "http://www.urlshortener.com:8000")

def wildcard_redirect(request, path_value = None):
    new_url = DEFAULT_REDIRECT_PATH
    if path_value is not None:
        new_url = DEFAULT_REDIRECT_PATH + "/" + path_value
    return HttpResponseRedirect(new_url)
