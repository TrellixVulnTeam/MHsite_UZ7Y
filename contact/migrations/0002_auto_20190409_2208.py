# Generated by Django 2.1.4 on 2019-04-09 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='mensagem',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='primeiro_nome',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='second_name',
            new_name='segundo_nome',
        ),
    ]