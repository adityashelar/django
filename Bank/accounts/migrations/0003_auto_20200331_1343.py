# Generated by Django 3.0.4 on 2020-03-31 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200331_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.TextField(unique=True),
        ),
    ]
