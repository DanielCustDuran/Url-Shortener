from django.db import models

from shortener.models import URL

class ClickEventManager(models.Manager):
    """docstring for ClickEventManager."""
    def create_event(self, instace):
        if isinstance(URL, instace):
            obj, created = self.objects.get_or_create(url = instace)
            obj.count += 1
            obj.save()
            return obj.count
        return None

# Create your models here.
class ClickEvent(models.Model):
    """docstring for ClickEvent."""
    shortener_url = models.OneToOneField(URL, on_delete = models.CASCADE)
    count = models.IntegerField(default = 0)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i = self.count)
