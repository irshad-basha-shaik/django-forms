# Generated by Django 3.2.9 on 2021-11-19 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetapp', '0022_auto_20211118_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetmodel',
            name='domain_workgoup',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='gef_id_number',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='hdd',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='machine_model_no',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='machine_type',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='make1',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='make2',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='model',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='ram',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='serial_no1',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='assetmodel',
            name='serial_no2',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
