# Generated by Django 2.1.4 on 2019-04-10 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0026_auto_20190409_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
