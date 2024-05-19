# Generated by Django 5.0.6 on 2024-05-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_tickets_description_m'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='description',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
