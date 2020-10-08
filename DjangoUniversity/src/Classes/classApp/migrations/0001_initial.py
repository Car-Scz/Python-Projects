# Generated by Django 3.1.2 on 2020-10-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('courseID', models.IntegerField(default=0)),
                ('instructorName', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.FloatField(max_length=6)),
            ],
        ),
    ]