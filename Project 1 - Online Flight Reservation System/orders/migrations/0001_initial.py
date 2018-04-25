# Generated by Django 2.0.3 on 2018-03-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_no', models.CharField(blank=True, max_length=100)),
                ('leg_no', models.IntegerField(null=True)),
                ('airline_id', models.CharField(blank=True, max_length=3)),
                ('flight_no', models.IntegerField(null=True)),
                ('stop_no', models.IntegerField(null=True)),
                ('seat_num', models.IntegerField(null=True)),
                ('src_time', models.DateTimeField(blank=True)),
                ('dst_time', models.DateTimeField(blank=True)),
                ('cabin', models.CharField(blank=True, max_length=20)),
                ('meal_preference', models.CharField(blank=True, max_length=100)),
                ('src_airport', models.CharField(blank=True, max_length=4)),
                ('dst_airport', models.CharField(blank=True, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_no', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('reservation_date', models.DateTimeField(auto_now_add=True)),
                ('reservation_status', models.CharField(choices=[('A', 'Accepted'), ('C', 'Cancelled')], default='A', max_length=20)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('num_legs', models.IntegerField(null=True)),
                ('fare_restrictions', models.CharField(blank=True, max_length=100)),
                ('passengers', models.CharField(blank=True, max_length=100)),
                ('total_fare', models.FloatField(blank=True)),
                ('booking_fee', models.FloatField(blank=True)),
                ('customer_rep', models.CharField(blank=True, max_length=25)),
            ],
        ),
    ]