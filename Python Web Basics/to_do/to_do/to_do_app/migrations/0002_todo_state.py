# Generated by Django 3.2.4 on 2021-06-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
