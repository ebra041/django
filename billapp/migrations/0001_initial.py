# Generated by Django 4.2.7 on 2023-11-14 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bdate', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BillOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billapp.bill')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billapp.food')),
            ],
        ),
    ]
