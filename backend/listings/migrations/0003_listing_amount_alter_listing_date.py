# Generated by Django 4.0.2 on 2022-03-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='amount',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateField(),
        ),
    ]
