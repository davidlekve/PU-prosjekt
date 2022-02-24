# Generated by Django 4.0.2 on 2022-02-17 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(choices=[('oslo', 'Oslo'), ('trondheim', 'Trondheim'), ('stavanger', 'Stavanger'), ('bergen', 'Bergen')], max_length=9)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('b', 'Buy'), ('s', 'Sell')], max_length=1)),
                ('complete', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
