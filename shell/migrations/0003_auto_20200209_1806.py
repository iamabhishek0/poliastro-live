# Generated by Django 3.0.2 on 2020-02-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0002_auto_20200209_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searches',
            name='private',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='searches',
            name='query',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
