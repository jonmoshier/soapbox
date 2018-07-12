from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from landingpage.models import LandingPage
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404

class IndexView(ListView):
    model = LandingPage
    context_object_name = "landingpages"

class LandingPageView(DetailView):
    model = LandingPage
    template_name = "landingpage/landingpage_detail.html"
    context_object_name = "landingpage"