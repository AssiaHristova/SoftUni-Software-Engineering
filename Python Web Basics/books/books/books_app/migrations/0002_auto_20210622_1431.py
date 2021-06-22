# Generated by Django 3.2.4 on 2021-06-22 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
