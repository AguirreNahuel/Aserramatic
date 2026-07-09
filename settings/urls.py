from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings_panel, name='settings_panel'),
]