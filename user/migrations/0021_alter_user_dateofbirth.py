# Generated by Django 3.2.9 on 2021-12-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20211224_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='DateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]