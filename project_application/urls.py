from django.urls import path
from . import views

#Used for template tagging
app_name = 'project_application'

urlpatterns = [
    #name = '' is used for connecting with {% url %} in tamplates
    path('o-nas/', views.about, name='about'),
    path('kontakt/', views.contact, name='contact'),
    path('zglos/', views.businesses, name='form'),
    path('odkrywaj/', views.explore, name='explore'),
]
