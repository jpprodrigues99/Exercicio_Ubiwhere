# Generated by Django 5.1 on 2024-08-16 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoadSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrafficReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_speed', models.FloatField()),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='traffic.roadsegment')),
            ],
        ),
    ]
