# Generated by Django 3.1.5 on 2021-01-26 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210125_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(to='accounts.UserRoles'),
        ),
    ]
