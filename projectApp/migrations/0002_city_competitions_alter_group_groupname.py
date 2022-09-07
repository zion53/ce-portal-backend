# Generated by Django 4.0.6 on 2022-09-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='competitions',
            field=models.ManyToManyField(to='projectApp.competition'),
        ),
        migrations.AlterField(
            model_name='group',
            name='groupName',
            field=models.TextField(max_length=50),
        ),
    ]
