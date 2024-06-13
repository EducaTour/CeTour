# Generated by Django 5.0.6 on 2024-06-02 18:27

import prediction.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=200)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.URLField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
