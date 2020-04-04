from django.db import models
import datetime

# Create your models here.
class Business(models.Model):
    """docstring for Business."""
    class Meta():
        verbose_name_plural = "Businesses"

    name = models.CharField("Nazwa",max_length = 264, unique = True)
    AVAILABLE_TYPES = (
        ('Kawiarnia', 'Kawiarnia'),
        ('Restauracja', 'Restauracja'),
        ('Bar', 'Bar'),
        ('Inny', 'Inny'),
    )
    type = models.CharField("Kategoria",max_length = 264, choices = AVAILABLE_TYPES)
    AVAILABLE_FORMS = (
        ('Karta podarunkowa', 'Karta podarunkowa'),
        ('Zniżka', 'Zniżka'),
        ('Zawieszony produkt', 'Zawieszony produkt (np.kawa)'),
        ('Inna', 'Inna'),
    )
    form = models.CharField("Rodzaj wsparcia",max_length = 264, choices = AVAILABLE_FORMS)
    url = models.URLField("URL",max_length=200)
    city = models.CharField("Miasto",max_length = 264)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class NewsletterSubscriber(models.Model):
    """docstring for Newsletter."""
    class Meta():
        verbose_name_plural = "Newsletter Subscribers"

    email = models.EmailField(unique=True)
    name = models.CharField(max_length = 264)
    starting_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
