from django import forms
from django.forms import TextInput

from .models import Business, NewsletterSubscriber


names = ["Cafe Kryzysowa", "Pizzeria u Pomocnego", "Biały kot", "Pełnia"]
cities = ["Warszawa", "Kraków", "Poznań", "Radom","Wrocław","Gdańsk"]
urls = ["kryzysowa.pl","u-pomocnego.pl","bialy-kot.pl"]

import random


class NewBusiness(forms.ModelForm):
    """docstring for  New Business"""
    class Meta():
        model = Business
        exclude = ('update_date',)

        widgets = {
            'url':TextInput(),
            'name': forms.TextInput(attrs={'placeholder': random.choice(names)}),
            'city': forms.TextInput(attrs={'placeholder': random.choice(cities)}),
            'url': forms.TextInput(attrs={'placeholder': random.choice(urls)}),
        }
class NewNewsletterSubscriber(forms.ModelForm):
    """docstring for New Newsletter Subscriber"""
    class Meta():
        model = NewsletterSubscriber
        exclude = ('starting_date',)
