# Generated by Django 5.1 on 2024-08-25 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('icon', models.CharField(blank=True, max_length=125, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='myport/%Y/%m/%d')),
                ('price', models.CharField(blank=True, max_length=225, null=True)),
                ('content', models.IntegerField(blank=True, max_length=225, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='menu.category')),
            ],
        ),
    ]
