# Generated by Django 2.2.2 on 2019-06-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20190609_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top_headline',
            name='auther',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='top_headline',
            name='category',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='top_headline',
            name='publishedAt',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='top_headline',
            name='source_name',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='top_headline',
            name='upload_date',
            field=models.CharField(max_length=256),
        ),
    ]
