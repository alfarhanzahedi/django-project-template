from django.urls import path
from django.contrib.auth import views as auth_views

from .views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name = 'landing_page'),
]