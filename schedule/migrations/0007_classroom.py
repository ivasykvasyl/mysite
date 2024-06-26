# Generated by Django 5.0.6 on 2024-06-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=64)),
                ('learn3', models.ManyToManyField(blank=True, related_name='classroom', to='schedule.daysoftheweek')),
            ],
        ),
    ]
