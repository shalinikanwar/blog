# Generated by Django 3.2.15 on 2022-08-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0003_auto_20220819_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='optionc',
            field=models.FileField(upload_to='blog_image/'),
        ),
    ]
