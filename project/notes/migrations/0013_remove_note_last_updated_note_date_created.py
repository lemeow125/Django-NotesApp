# Generated by Django 4.1.7 on 2023-03-04 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_remove_note_date_created_note_last_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]