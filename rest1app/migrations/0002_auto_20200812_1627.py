# Generated by Django 3.1 on 2020-08-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest1app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=2),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=2),
        ),
    ]
