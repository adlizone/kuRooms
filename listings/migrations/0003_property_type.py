# Generated by Django 5.0.6 on 2024-07-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_property_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='type',
            field=models.CharField(blank=True, choices=[(1, 'PG for boys'), (2, 'PG for girls')], max_length=100, null=True),
        ),
    ]