# Generated by Django 5.1 on 2024-08-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='content',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
