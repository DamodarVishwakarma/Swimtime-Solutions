# Generated by Django 3.1.1 on 2021-03-31 12:04

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
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('booking_type', models.CharField(choices=[('1', 'Booked'), ('3', 'Denied'), ('2', 'Blocked By Instructor')], max_length=1)),
                ('booking_payment_status', models.CharField(choices=[('1', 'COMPLETED'), ('0', 'PARTIALLY BOOKED')], default='0', max_length=1)),
                ('paper_work', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Completed')], max_length=1)),
                ('payment_type', models.CharField(choices=[('1', 'Cash'), ('2', 'Card')], max_length=1)),
                ('total_amount', models.IntegerField()),
                ('paid_amount', models.IntegerField()),
                ('due_amount', models.IntegerField()),
                ('payment_at', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appointment.booking')),
            ],
        ),
        migrations.CreateModel(
            name='ClassInstructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time_slot', models.IntegerField()),
                ('total_days', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('thumbnail_image', models.ImageField(blank=True, default='Images/Classes/swim.jpeg', null=True, upload_to='Images/Classes')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='class_instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appointment.classinstructor'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('1', 'Scheduled'), ('2', 'Completed'), ('3', 'Canceled')], default='1', max_length=1)),
                ('remark', models.CharField(blank=True, max_length=300, null=True)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Appointment.booking')),
            ],
        ),
    ]