from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin header customization
admin.site.site_title = "Jacquan's Dashboard"
admin.site.site_header = "Login to Jacquan Portfolio"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
]