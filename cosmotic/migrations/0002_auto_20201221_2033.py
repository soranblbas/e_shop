# Generated by Django 3.1.4 on 2020-12-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmotic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateTimeField(),
        ),
    ]
