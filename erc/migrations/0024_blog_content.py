# Generated by Django 2.2.3 on 2019-07-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erc', '0023_auto_20190721_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, default="Don't know", null=True),
        ),
    ]
