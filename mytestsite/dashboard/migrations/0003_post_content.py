# Generated by Django 3.2.8 on 2021-10-29 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]
