# Generated by Django 3.1.2 on 2020-10-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='courseID',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
