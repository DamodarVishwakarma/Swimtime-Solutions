# Generated by Django 3.2.9 on 2022-02-03 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_kids'),
        ('Appointment', '0004_auto_20210526_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='kids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.kids'),
        ),
    ]
