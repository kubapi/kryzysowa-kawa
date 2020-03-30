from django.urls import path
from . import views

#Used for template tagging
app_name = 'project_application'

urlpatterns = [
    #name = '' is used for connecting with {% url %} in tamplates
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.businesses, name='form')
]
