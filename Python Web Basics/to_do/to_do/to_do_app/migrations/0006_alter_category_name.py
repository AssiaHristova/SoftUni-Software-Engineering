# Generated by Django 3.2.4 on 2021-06-11 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0005_auto_20210611_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Home', 'Home_stuff'), ('Work', 'Work_stuff'), ('Leisure', 'Leisure_stuff')], max_length=20),
        ),
    ]
