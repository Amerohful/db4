# Generated by Django 2.2.7 on 2019-11-24 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_library', '0002_book_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='pasport',
            new_name='passport',
        ),
    ]
