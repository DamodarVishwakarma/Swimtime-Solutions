# Generated by Django 3.1.1 on 2021-04-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20210408_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Instructor'), (2, 'Trainee'), (3, 'Admin')], default=2),
        ),
    ]