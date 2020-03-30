from django import forms
from .models import Business, NewsletterSubscriber

class NewBusiness(forms.ModelForm):
    """docstring for  New Business"""
    class Meta():
        model = Business
        exclude = ('update_date',)

class NewNewsletterSubscriber(forms.ModelForm):
    """docstring for New Newsletter Subscriber"""
    class Meta():
        model = NewsletterSubscriber
        exclude = ('starting_date',)
