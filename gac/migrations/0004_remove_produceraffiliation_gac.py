# Generated by Django 4.1 on 2022-11-18 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gac', '0003_marketplace_alter_produceraffiliation_gac_delete_gac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produceraffiliation',
            name='gac',
        ),
    ]