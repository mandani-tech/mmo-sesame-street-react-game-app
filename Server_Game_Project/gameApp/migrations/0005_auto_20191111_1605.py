# Generated by Django 2.0.6 on 2019-11-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameApp', '0004_usermodel_useravatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='userAttack',
            field=models.IntegerField(default=45),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='userHealth',
            field=models.IntegerField(default=149),
        ),
    ]