# Generated by Django 2.2.7 on 2019-11-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_library', '0003_auto_20191124_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='return_book',
            field=models.BooleanField(default=False),
        ),
    ]
