# Generated by Django 4.2.7 on 2023-11-17 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0005_bill_foods_food_bills_alter_billorders_bill_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billorders',
            name='quantity',
        ),
    ]
