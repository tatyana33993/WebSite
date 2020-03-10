# Generated by Django 3.0 on 2019-12-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('number', models.CharField(max_length=11)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('table', models.IntegerField()),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('count_seats', models.IntegerField()),
            ],
        ),
    ]
