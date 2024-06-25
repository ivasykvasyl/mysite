# Generated by Django 5.0.6 on 2024-06-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_discipline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=5)),
                ('learn', models.ManyToManyField(blank=True, related_name='time', to='schedule.daysoftheweek')),
            ],
        ),
    ]
