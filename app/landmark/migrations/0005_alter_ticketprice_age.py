# Generated by Django 4.2.3 on 2024-06-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmark', '0004_language_remove_landmark_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketprice',
            name='age',
            field=models.CharField(max_length=50),
        ),
    ]
