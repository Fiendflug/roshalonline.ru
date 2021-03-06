# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ro_app', '0002_auto_20170725_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationcategory',
            name='image',
            field=models.ImageField(default=None, help_text='Рекомендуемый размер изображения - 640 на 400 пикселей', upload_to='ro_app/content/images/default_category_news_images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='notice',
            name='default_image',
            field=models.BooleanField(default=True, help_text='Укажите использовать ли изображение по умолчанию исходя из категории новости', verbose_name='Изображение по умолчанию'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(default=None, help_text='Рекомендуемый размер изображения - 640 на 400 пикселей', upload_to='ro_app/content/images/news_images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='toppageinformation',
            name='image',
            field=models.ImageField(help_text='Рекомендуемый размер изображения - 920 на 720 пикселей', upload_to='ro_app/content/images/top_page_images/', verbose_name='Изображение'),
        ),
    ]
