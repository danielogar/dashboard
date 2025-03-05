from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('config/', views.config_settings, name='config_settings'),
]
