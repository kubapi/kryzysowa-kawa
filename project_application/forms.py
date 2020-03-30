from django import forms
from django.forms import TextInput

from .models import Business, NewsletterSubscriber

class NewBusiness(forms.ModelForm):
    """docstring for  New Business"""
    class Meta():
        model = Business
        exclude = ('update_date',)

        widgets = {
            'url':TextInput(),
        }
class NewNewsletterSubscriber(forms.ModelForm):
    """docstring for New Newsletter Subscriber"""
    class Meta():
        model = NewsletterSubscriber
        exclude = ('starting_date',)
