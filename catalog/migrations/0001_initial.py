# Generated by Django 2.2 on 2019-04-28 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('firstname', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('school', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
