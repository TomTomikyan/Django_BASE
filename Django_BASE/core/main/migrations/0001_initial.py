# Generated by Django 5.0.6 on 2024-05-11 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='cat name')),
                ('img', models.ImageField(upload_to='category/', verbose_name='cat image')),
            ],
        ),
        migrations.CreateModel(
            name='prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='prod name')),
                ('img', models.ImageField(upload_to='product/', verbose_name='prod image')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod', to='main.cat')),
            ],
        ),
    ]
