# Generated by Django 5.1.1 on 2024-09-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurucon', '0002_masterofconference_alter_speaker_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
