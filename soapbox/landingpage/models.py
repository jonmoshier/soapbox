from django.db import models
from blueprint.models import Blueprint
from django.utils.text import slugify

def default_landing_page():
    return "Default"

class LandingPage(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, blank=True)

    def __str__(self):
        return self.name
        
class URL(models.Model):
    url = models.URLField(max_length=200)
    parent = models.ForeignKey(LandingPage, on_delete=models.CASCADE)