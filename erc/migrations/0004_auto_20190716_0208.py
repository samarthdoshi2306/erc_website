# Generated by Django 2.2.3 on 2019-07-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erc', '0003_event_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='problem_statement',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='video',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.CharField(max_length=100),
        ),
    ]
