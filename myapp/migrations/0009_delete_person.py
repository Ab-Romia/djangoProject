# Generated by Django 4.2.4 on 2023-09-11 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_booking_reservation_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]