# Generated by Django 4.1.2 on 2024-05-02 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carDetails', '0003_cartparts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartParts',
            new_name='CarParts',
        ),
    ]
