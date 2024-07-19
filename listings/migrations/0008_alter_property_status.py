# Generated by Django 5.0.6 on 2024-07-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_property_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(blank=True, choices=[('Rooms Available', 'Rooms Available'), ('Rooms Not-available', 'Rooms Not-Available')], max_length=20, null=True),
        ),
    ]
