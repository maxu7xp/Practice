# Generated by Django 5.1.3 on 2024-12-11 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maplocationmarkerss',
            name='MarkerLatitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maplocationmarkerss',
            name='MarkerLongtitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maplocationmarkerss',
            name='IsHuis',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='maplocationmarkerss',
            name='IsRave',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='maplocationmarkerss',
            name='isKantoor',
            field=models.FloatField(),
        ),
    ]
