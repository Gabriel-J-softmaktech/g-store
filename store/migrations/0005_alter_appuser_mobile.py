# Generated by Django 4.0.4 on 2022-07-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_appuser_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='mobile',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
