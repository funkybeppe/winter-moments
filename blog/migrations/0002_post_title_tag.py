# Generated by Django 3.2.17 on 2023-02-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Winter Moments', max_length=255),
        ),
    ]
