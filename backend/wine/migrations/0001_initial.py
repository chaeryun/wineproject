# Generated by Django 3.2.9 on 2022-04-01 06:23

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
            name='Wine',
            fields=[
                ('wine_id', models.IntegerField(primary_key=True, serialize=False)),
                ('wine', models.CharField(default='Unknown_Wine', max_length=500)),
                ('winery', models.CharField(default='Unknown_Winery', max_length=500)),
                ('country', models.CharField(default='Unknown_Country', max_length=500)),
                ('location', models.CharField(default='Unknown_Location', max_length=500)),
                ('image', models.URLField(default='Cannot_found_ImageURL')),
                ('color', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('light', models.FloatField()),
                ('smooth', models.FloatField()),
                ('dry', models.FloatField()),
                ('soft', models.FloatField()),
                ('gentle', models.FloatField()),
                ('taste', models.TextField(null=True)),
                ('food', models.TextField(null=True)),
                ('grapes', models.TextField(null=True)),
                ('alcohol', models.FloatField()),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Userlikewine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wine.wine')),
            ],
        ),
    ]
