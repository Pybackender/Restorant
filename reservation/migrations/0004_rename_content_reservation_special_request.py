# Generated by Django 5.1 on 2024-08-26 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_reservation_num_of_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='content',
            new_name='special_request',
        ),
    ]