# Generated by Django 3.2.5 on 2021-08-17 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]