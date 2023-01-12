# Generated by Django 4.1.5 on 2023-01-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value_per_bitcoin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=255)),
                ('expiration_date', models.CharField(max_length=255)),
                ('cvv', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]