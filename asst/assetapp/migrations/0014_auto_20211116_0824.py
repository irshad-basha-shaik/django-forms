# Generated by Django 3.2.5 on 2021-11-16 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0013_auto_20211116_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodel',
            name='amc_end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='amc_start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='processor_purchase_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='user_acceptance_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='user_handed_over_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='warranty_end_date',
            field=models.DateTimeField(),
        ),
    ]
