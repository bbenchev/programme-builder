# Generated by Django 2.0.2 on 2018-02-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_auto_20180224_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='prerequisites',
            field=models.ManyToManyField(to='builder.Module'),
        ),
    ]
