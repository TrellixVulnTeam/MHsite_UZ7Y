# Generated by Django 2.1.4 on 2019-03-22 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190226_2038'),
        ('payments', '0002_auto_20190318_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderByCTT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=17)),
                ('nome_completo', models.CharField(max_length=150)),
                ('morada', models.CharField(max_length=200)),
                ('codigo_postal_1', models.CharField(max_length=4)),
                ('codigo_postal_2', models.CharField(max_length=3)),
                ('is_ordered', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='OrderOnline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=17)),
                ('nome_completo', models.CharField(max_length=150)),
                ('morada', models.CharField(max_length=200)),
                ('codigo_postal_1', models.CharField(max_length=4)),
                ('codigo_postal_2', models.CharField(max_length=3)),
                ('is_ordered', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Cart')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]