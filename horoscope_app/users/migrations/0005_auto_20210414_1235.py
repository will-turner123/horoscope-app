# Generated by Django 3.1.7 on 2021-04-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210413_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sign',
            field=models.CharField(default='No sign', max_length=15),
        ),
    ]