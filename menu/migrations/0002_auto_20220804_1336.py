# Generated by Django 3.2.9 on 2022-08-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='items_menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='items_menu', to='item.Item'),
        ),
    ]
