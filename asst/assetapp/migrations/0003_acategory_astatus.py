# Generated by Django 3.2.5 on 2021-10-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0002_auto_20211029_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Astatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asname', models.CharField(max_length=100)),
            ],
        ),
    ]