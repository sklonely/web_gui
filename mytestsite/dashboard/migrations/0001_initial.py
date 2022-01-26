# Generated by Django 3.2.8 on 2021-12-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('machine_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('work_no', models.CharField(max_length=100, null=True)),
                ('principal', models.CharField(max_length=100, null=True)),
                ('production_capacity', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('need_production_capacity', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('check_nums', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('good_production', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('fiex_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
