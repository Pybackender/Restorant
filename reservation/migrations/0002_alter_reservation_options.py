# Generated by Django 5.1 on 2024-08-25 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'reservation', 'verbose_name_plural': 'reservations'},
        ),
    ]