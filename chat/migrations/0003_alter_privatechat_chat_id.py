# Generated by Django 4.2.4 on 2023-09-03 23:15

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_privatechat_alter_groupchat_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatechat',
            name='chat_id',
            field=models.CharField(default=chat.models.unique_private_chat_id, max_length=64),
        ),
    ]
