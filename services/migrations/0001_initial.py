# Generated by Django 4.1.1 on 2022-09-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
