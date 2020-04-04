from django import forms
from django.forms import TextInput

from .models import Business, NewsletterSubscriber
from django.core import validators

names = ["Cafe Kryzysowa", "Pizzeria u Pomocnego", "Biały kot", "Pełnia"]
cities = ["Warszawa", "Kraków", "Poznań", "Radom","Wrocław","Gdańsk"]
urls = ["kryzysowa.pl","u-pomocnego.pl","bialy-kot.pl"]

import random


class NewBusiness(forms.ModelForm):
    """docstring for  New Business"""
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = Business
        exclude = ('update_date',)

        widgets = {
            'url':TextInput(),
            'name': forms.TextInput(attrs={'placeholder': random.choice(names)}),
            'city': forms.TextInput(attrs={'placeholder': random.choice(cities)}),
            'url': forms.TextInput(attrs={'placeholder': random.choice(urls)}),
        }


nsnames = ["Jan Kowalski", "Zygmunt Nowak", "Kacper Lewandowski"]
nsemails = ["jan.kowalski@gmail.com","kryzysowa@gmail.com", "u-pomocnego@wp.pl","pełnia.kontakt@onet.pl"]
class NewNewsletterSubscriber(forms.ModelForm):
    """docstring for New Newsletter Subscriber"""
    class Meta():
        model = NewsletterSubscriber
        exclude = ('starting_date',)

        widgets = {
           'name': forms.TextInput(attrs={'placeholder': random.choice(nsnames)}),
           'email': forms.TextInput(attrs={'placeholder': random.choice(nsemails)}),
        }
