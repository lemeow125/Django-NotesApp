# Generated by Django 4.1.7 on 2023-03-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_alter_note_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(),
        ),
    ]
