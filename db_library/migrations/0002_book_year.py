# Generated by Django 2.2.7 on 2019-11-24 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
