# Generated by Django 4.2.4 on 2023-09-11 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_delete_elmenu_delete_menucategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Logger',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]