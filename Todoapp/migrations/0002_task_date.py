# Generated by Django 3.2.12 on 2022-04-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-03-03'),
            preserve_default=False,
        ),
    ]
