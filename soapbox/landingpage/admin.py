from django.contrib import admin
from .models import LandingPage, URL

class LandingPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    child_models = (URL,)
admin.site.register(LandingPage, LandingPageAdmin)