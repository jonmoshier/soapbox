from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('<slug>', views.LandingPageView.as_view()),
]
