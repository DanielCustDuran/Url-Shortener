from django.db import models

# Create your models here.

class URL(models.Model):
    """docstring for ."""
    url = models.CharField(max_length = 220, )

    def __str__(self):
        return str(self.url)
