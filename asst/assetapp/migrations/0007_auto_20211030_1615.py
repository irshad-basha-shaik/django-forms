# Generated by Django 3.2.5 on 2021-10-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0006_auto_20211030_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('licence', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='adress',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='location',
            name='owner',
            field=models.CharField(max_length=100),
        ),
    ]
