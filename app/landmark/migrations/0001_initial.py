# Generated by Django 4.2.3 on 2024-06-02 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('history', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('location_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UniqueActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('landmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='landmark.landmark')),
            ],
        ),
        migrations.CreateModel(
            name='TicketPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('landmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_prices', to='landmark.landmark')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLandmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.URLField()),
                ('landmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='landmark.landmark')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('landmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opening_hours', to='landmark.landmark')),
            ],
        ),
        migrations.AddField(
            model_name='landmark',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='landmark', to='landmark.location'),
        ),
    ]