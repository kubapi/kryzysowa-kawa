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
        ('Mały biznes', 'Mały biznes'),
        ('Księgarnia', 'Księgarnia'),
        ('Sklep z ubraniami', 'Sklep z ubraniami'),
        ('Sklep plastyczny', 'Sklep plastyczny'),
        ('Zoo', 'Zoo'),
        ('Sklep dla zwierząt', 'Sklep dla zwierząt'),
        ('Piekarnia', 'Piekarnia'),
        ('Sklep krawiecki', 'Sklep krawiecki'),
        ('Bazar', 'Bazar'),
        ('Garmażeria', 'Garmażeria'),
        ('Bar mleczny', 'Bar mleczny'),
        ('Kino', 'Kino'),
        ('Inny', 'Inny'),
    )
    type = models.CharField("Kategoria",max_length = 264, choices = AVAILABLE_TYPES)
    AVAILABLE_FORMS = (
        ('Karta podarunkowa', 'Karta podarunkowa'),
        ('Zniżka', 'Zniżka'),
        ('Zawieszony produkt', 'Zawieszony produkt (np.kawa)'),
        ('Produkt', 'Produkt'),
        ('Subskrypcja', 'Subskrypcja'),
        ('Zakupy online', 'Zakupy online'),
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

    email = models.EmailField("Email",unique=True)
    name = models.CharField("Imię",max_length = 264)
    starting_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
