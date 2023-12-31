# Generated by Django 4.2.4 on 2023-09-03 20:03

import account.models
from django.db import migrations, models
import extention.name_changer


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=extention.name_changer.upload_user_img_path),
        ),
        migrations.AddField(
            model_name='user',
            name='user_bio',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=account.models.unique_id, max_length=12, unique=True),
        ),
    ]
