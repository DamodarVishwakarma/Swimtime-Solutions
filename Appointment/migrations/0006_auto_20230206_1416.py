# Generated by Django 3.2.9 on 2023-02-06 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0005_booking_kids'),
    ]

    operations = [
        migrations.AddField(
            model_name='classinstructor',
            name='class_payment_range',
            field=models.IntegerField(blank=True, default=50, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myBooking', to='Appointment.booking'),
        ),
    ]
