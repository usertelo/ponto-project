# Generated by Django 2.0.2 on 2019-10-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='use',
            field=models.TextField(default='vazio'),
        ),
    ]