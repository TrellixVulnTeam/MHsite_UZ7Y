# Generated by Django 2.1.4 on 2019-02-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20190222_2239'),
        ('users', '0003_auto_20190224_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='items',
            field=models.ManyToManyField(blank=True, to='catalog.Item'),
        ),
    ]
