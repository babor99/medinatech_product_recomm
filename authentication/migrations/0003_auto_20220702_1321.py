# Generated by Django 3.2.13 on 2022-07-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20220702_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='lat',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='lon',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
    ]
