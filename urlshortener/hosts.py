from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name = 'www'),
    host(r'live', 'urlshortener.hostsconf.urls', name = 'live'),
    host(r'(?!www).*', 'urlshortener.hostsconf.urls', name = 'wildcard'),
)
