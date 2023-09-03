# Generated by Django 4.2.4 on 2023-09-03 23:16

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_privatechat_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchat',
            name='chat_id',
            field=models.CharField(default=chat.models.unique_group_chat_id, max_length=64),
        ),
    ]