# Generated by Django 3.0.2 on 2020-02-17 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=15)),
                ('City', models.CharField(max_length=15)),
                ('Address', models.CharField(max_length=256)),
                ('KindofHome', models.CharField(max_length=15)),
                ('RoomType', models.CharField(max_length=15)),
                ('Capacity', models.PositiveIntegerField()),
                ('Description', models.TextField()),
                ('PlacePhoto', models.ImageField(blank=True, upload_to='static')),
                ('Price', models.PositiveIntegerField()),
                ('RequestedToRent', models.BooleanField(default=False)),
                ('rented', models.BooleanField(default=False)),
                ('Pets', models.BooleanField(default=False)),
                ('Kids', models.BooleanField(default=False)),
                ('SmokingAllowed', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Arrival', models.DateField()),
                ('Depart', models.DateField()),
                ('AcceptanceByHost', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='placeandbooking.Place')),
            ],
        ),
    ]
