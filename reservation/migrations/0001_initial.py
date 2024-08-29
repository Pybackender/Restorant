# Generated by Django 5.1 on 2024-08-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=125, null=True)),
                ('email', models.EmailField(blank=True, max_length=125, null=True)),
                ('datetime', models.DateTimeField()),
                ('content', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
    ]