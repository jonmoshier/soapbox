from django.contrib import admin
from .models import Blueprint

class BlueprintAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blueprint, BlueprintAdmin)