# Generated by Django 3.2.9 on 2021-12-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookCab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='group',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
