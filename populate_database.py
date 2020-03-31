import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from project_application.models import Business, NewsletterSubscriber
from faker import Faker
