# Generated by Django 4.2.4 on 2023-09-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_practicemodel_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicemodel',
            name='user_image',
            field=models.FileField(default=2, upload_to='images'),
            preserve_default=False,
        ),
    ]