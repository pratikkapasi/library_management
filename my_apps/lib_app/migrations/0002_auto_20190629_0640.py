# Generated by Django 2.2.2 on 2019-06-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateField(),
        ),
    ]
