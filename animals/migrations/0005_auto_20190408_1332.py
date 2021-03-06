# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-08 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='status_choices',
            field=models.CharField(choices=[('Critically Endangered', 'CE'), ('Endangered', 'E'), ('Vulnerable', 'V'), ('Near Threatened', 'NT'), ('Least Concern', 'LC')], default='Critically Endangered', max_length=30),
        ),
    ]
