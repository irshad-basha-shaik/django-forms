# Generated by Django 3.2.5 on 2021-11-16 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0015_auto_20211116_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmodel',
            name='access',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='adobe_acrobate',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='antivirus',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='autocad',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='sap',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='assetmodel',
            name='visio',
            field=models.BooleanField(),
        ),
    ]
