# Generated by Django 5.0.6 on 2024-06-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_alter_time_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vykladach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vykladach', models.CharField(max_length=64)),
                ('learn1', models.ManyToManyField(blank=True, related_name='vykladach', to='schedule.daysoftheweek')),
            ],
        ),
    ]
