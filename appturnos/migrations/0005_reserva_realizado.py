# Generated by Django 5.0 on 2023-12-13 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appturnos', '0004_reserva_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='realizado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
