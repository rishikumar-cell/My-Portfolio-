from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
     path('', views.index, name='contact'),  # This handles both GET and POST
    path('success/', lambda request: render(request, 'success.html'), name='contact_success'),
]
