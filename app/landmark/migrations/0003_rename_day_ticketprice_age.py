# Generated by Django 4.2.3 on 2024-06-03 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landmark', '0002_alter_uniqueactivity_landmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketprice',
            old_name='day',
            new_name='age',
        ),
    ]
