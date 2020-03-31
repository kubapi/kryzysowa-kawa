import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zawieszona_kawa.settings')

import django
django.setup()

import random
from project_application.models import Business, NewsletterSubscriber
from faker import Faker

fakegen = Faker()
types = ["Kawiarnia", "Restauracja", "Bar", "Inny"]
forms = ["Karta podarunkowa", "Zniżka", "Zawieszony produkt", "Inna"]

def add_business():
    fake_name = fakegen.company()
    fake_type = random.choice(types)
    fake_form = random.choice(forms)
    fake_url = fakegen.url(schemes=None)
    fake_city = fakegen.city()

    b = Business.objects.get_or_create(name = fake_name, type = fake_type,
                                       form = fake_form, url = fake_url,
                                       city = fake_city)[0]
    b.save()
    return b


def add_newslettersubscriber():
    fake_email = fakegen.email()
    fake_name = fakegen.name()

    ns = NewsletterSubscriber.objects.get_or_create(email = fake_email, name = fake_name)[0]
    ns.save()
    return ns


def populate(business = True, newslettersubscriber = True,N = 20):
    for entry in range(N):
        if business:
            add_business()
        if newslettersubscriber:
            add_newslettersubscriber()


if __name__ == '__main__':
    print("Starting fake populating of database (%trial only%)")
    print("Populate Business? [0/1]")
    b = input()
    print("Populate NewsletterSubscriber? [0/1]")
    ns = input()
    print("How many records?")
    nr = input()
    populate(int(b), int(ns), int(nr))
    print("Populating completed!")
