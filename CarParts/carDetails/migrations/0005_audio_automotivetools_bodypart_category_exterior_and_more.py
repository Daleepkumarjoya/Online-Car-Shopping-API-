# Generated by Django 4.1.2 on 2024-05-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carDetails', '0004_rename_cartparts_carparts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AudioName', models.CharField(max_length=100)),
                ('AudioImage', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='AutomotiveTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AutomotiveToolsName', models.CharField(max_length=100)),
                ('AutomotiveToolsImage', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BodyPartName', models.CharField(max_length=100)),
                ('BodyPartImage', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100)),
                ('CategoryImage', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Exterior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExteriorName', models.CharField(max_length=100)),
                ('ExteriorImage', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InteriorName', models.CharField(max_length=100)),
                ('InteriorImage', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='lighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lightingName', models.CharField(max_length=100)),
                ('lightingImage', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopCarName', models.CharField(max_length=100)),
                ('ShopCarImage', models.ImageField(upload_to='images')),
                ('OffInPercentage', models.IntegerField(default=0)),
                ('CarDetail', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TireWheels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TireWheelsName', models.CharField(max_length=100)),
                ('TireWheelsImage', models.ImageField(upload_to='images')),
            ],
        ),
    ]
