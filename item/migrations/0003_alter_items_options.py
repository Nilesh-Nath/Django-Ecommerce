# Generated by Django 5.1.1 on 2024-10-10 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_categories_options_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name_plural': 'Items'},
        ),
    ]
