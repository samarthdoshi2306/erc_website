# Generated by Django 2.2.3 on 2019-07-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erc', '0018_auto_20190721_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='filterClass',
            field=models.CharField(choices=[(1, 'Unread'), (2, 'Read')], default=1, max_length=80),
        ),
    ]