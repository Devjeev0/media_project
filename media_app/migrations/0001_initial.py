# Generated by Django 3.2 on 2023-05-22 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='timing_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_time', models.TimeField()),
                ('ending_time', models.TimeField()),
                ('starting_date', models.DateField(null=True)),
                ('ending_date', models.DateTimeField(null=True)),
                ('duration', models.DurationField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='team_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(default='', max_length=30)),
                ('name', models.CharField(default='', max_length=30)),
                ('work_description', models.TextField(default='')),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_app.room_model')),
                ('Time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_app.timing_model')),
            ],
        ),
    ]
