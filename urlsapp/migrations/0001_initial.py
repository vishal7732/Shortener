# Generated by Django 3.2.4 on 2021-06-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.CharField(max_length=400, unique=True)),
                ('short_url', models.CharField(max_length=40, unique=True)),
            ],
        ),
    ]