from django.db import models

from .utils import code_generator, create_shortcode
# Create your models here.

class URLManager(models.Manager):
    """docstring for URLManager."""
    def all(self, *args,**kwargs):
        qs = super(URLManager, self).all(*args, **kwargs).filter(active = False)
        return qs

    def refresh_shortcodes(self, items = None):
        qs = URL.objects.filter(id__gte = 1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return ("New codes made: {i}".format(i = new_codes ))

class URL(models.Model):
    """docstring for ."""
    url = models.CharField(max_length = 220, )
    shortcode = models.CharField(max_length = 15, unique = True, blank = True)
    update = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = True)
    objects = URLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
