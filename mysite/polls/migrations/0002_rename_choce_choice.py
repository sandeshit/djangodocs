# Generated by Django 4.2.11 on 2024-07-12 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choce',
            new_name='Choice',
        ),
    ]
