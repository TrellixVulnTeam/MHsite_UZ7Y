# Generated by Django 2.1.4 on 2019-04-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0023_auto_20190408_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbyctt',
            name='ordered_through',
            field=models.CharField(default='', max_length=10),
        ),
    ]