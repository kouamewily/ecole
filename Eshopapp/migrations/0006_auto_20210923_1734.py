# Generated by Django 3.2.7 on 2021-09-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshopapp', '0005_auto_20210923_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='adresse',
        ),
        migrations.AddField(
            model_name='order',
            name='add',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
