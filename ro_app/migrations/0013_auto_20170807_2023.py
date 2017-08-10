# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ro_app', '0012_auto_20170807_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationcategory',
            name='image',
            field=models.ImageField(default=None, help_text='Выберите изображение для категории, которое будет применяться ко  всем новостям категории без указания изображения .Рекомендуемый размер изображения - 640 на 400 пикселей', upload_to='images/default_category_news_images/', verbose_name='Изображение по умолчанию'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(blank=True, default=None, help_text='Рекомендуемый размер изображения - 640 на 400 пикселей', null=True, upload_to='images/news_images/', verbose_name='Изображение'),
        ),
    ]
