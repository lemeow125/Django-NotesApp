# Generated by Django 4.1.7 on 2023-03-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_remove_note_last_updated_note_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]