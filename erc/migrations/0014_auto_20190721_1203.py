# Generated by Django 2.2.2 on 2019-07-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erc', '0013_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='pdf',
            field=models.FileField(upload_to='media/news/pdfs'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='image',
            field=models.ImageField(upload_to='media/team'),
        ),
    ]
