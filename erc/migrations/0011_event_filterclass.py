# Generated by Django 2.2.2 on 2019-07-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erc', '0010_auto_20190719_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='filterClass',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
