# Generated by Django 3.2.12 on 2022-04-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
