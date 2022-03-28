# Generated by Django 3.2.9 on 2022-03-28 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('wine', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('winery', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('image', models.URLField()),
                ('color', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('light', models.FloatField()),
                ('smooth', models.FloatField()),
                ('dry', models.FloatField()),
                ('soft', models.FloatField()),
                ('gentle', models.FloatField()),
                ('taste', models.TextField(null=True)),
                ('food', models.TextField(null=True)),
                ('grapes', models.TextField(null=True)),
                ('alcohol', models.FloatField()),
            ],
        ),
    ]
