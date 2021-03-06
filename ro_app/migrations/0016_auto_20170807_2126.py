# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ro_app', '0015_auto_20170807_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internettarif',
            name='title',
            field=models.CharField(help_text='Укажите название для тарифа. Только строчные латинские буквы. Максимум 50 символов', max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(help_text='Укажите заголовок новости. Максимум 30 символов', max_length=70, verbose_name='Заголовок'),
        ),
    ]
