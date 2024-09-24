# Generated by Django 5.1.1 on 2024-09-24 06:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurucon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterOfConference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='speaker',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.FileField(upload_to='static/uploads/', validators=[django.core.validators.FileExtensionValidator(['svg', 'png', 'jpg', 'jpeg'])]),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('duration', models.TimeField()),
                ('description', models.TextField(blank=True)),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurucon.speaker')),
            ],
        ),
    ]
