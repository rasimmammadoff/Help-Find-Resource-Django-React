# Generated by Django 3.0.5 on 2020-04-19 18:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0024_url_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='urls',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(unique=True), size=None),
        ),
    ]
