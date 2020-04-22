# Generated by Django 3.0.3 on 2020-04-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_application', '0002_business_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='form',
            field=models.CharField(choices=[('Zbiórka', 'Zbiórka'), ('Voucher', 'Voucher'), ('Zajęcia', 'Zajęcia (kulinarne, rzemieślnicze...)'), ('Karta podarunkowa', 'Karta podarunkowa'), ('Wynajęcie food trucka', 'Wynajęcie food trucka'), ('Bony rabatowe', 'Bony rabatowe (zniżka)'), ('Zawieszony produkt', 'Zawieszony produkt (do odebrania po otwarciu)'), ('Zakupy online', 'Zakupy online'), ('Inna', 'Inna')], max_length=264, verbose_name='Rodzaj wsparcia'),
        ),
        migrations.AlterField(
            model_name='business',
            name='type',
            field=models.CharField(choices=[('Kawiarnia', 'Kawiarnia'), ('Restauracja', 'Restauracja'), ('Cukiernia', 'Cukiernia'), ('Bar', 'Bar'), ('Lokalny biznes', 'Lokalny biznes'), ('Księgarnia', 'Księgarnia'), ('Sklep z ubraniami', 'Sklep z ubraniami'), ('Sklep plastyczny', 'Sklep plastyczny'), ('Zoo', 'Zoo'), ('Sklep dla zwierząt', 'Sklep dla zwierząt'), ('Piekarnia', 'Piekarnia'), ('Sklep krawiecki', 'Sklep krawiecki'), ('Bazar', 'Bazar'), ('Garmażeria', 'Garmażeria'), ('Bar mleczny', 'Bar mleczny'), ('Salon', 'Salon'), ('Kino', 'Kino'), ('Klub', 'Klub'), ('Teatr', 'Teatr'), ('Sklep odzieżowy (Moda)', 'Sklep odzieżowy (Moda)'), ('Inny', 'Inny')], max_length=264, verbose_name='Kategoria'),
        ),
    ]