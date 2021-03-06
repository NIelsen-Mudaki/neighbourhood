# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-03-25 12:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('Admin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('admin_profile', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Profile')),
                ('neighborhood', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Neighborhood')),
            ],
            options={
                'verbose_name': 'My Business',
                'verbose_name_plural': 'Business',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-pub_date'], 'verbose_name': 'My Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
