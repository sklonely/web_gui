# Generated by Django 3.2.8 on 2022-01-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_post_starting_part_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='state_array',
            field=models.CharField(max_length=1440, null=True),
        ),
    ]
