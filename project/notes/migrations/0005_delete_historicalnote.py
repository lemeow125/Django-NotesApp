# Generated by Django 4.1.7 on 2023-02-24 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_historicalnote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalNote',
        ),
    ]
