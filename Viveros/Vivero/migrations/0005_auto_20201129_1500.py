# Generated by Django 2.2.12 on 2020-11-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vivero', '0004_vivero_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vivero',
            name='codigo',
            field=models.IntegerField(unique=True),
        ),
    ]
