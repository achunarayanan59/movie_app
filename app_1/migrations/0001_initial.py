# Generated by Django 5.1 on 2024-08-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('year', models.IntegerField(null=True)),
                ('desc', models.TextField(max_length=250)),
            ],
        ),
    ]
