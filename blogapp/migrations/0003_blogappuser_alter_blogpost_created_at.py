# Generated by Django 4.0.4 on 2022-05-20 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blogpost_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('profile', models.FileField(null=True, upload_to='images')),
                ('verification_code', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_removed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 20, 13, 42, 33, 571296))),
                ('updated_at', models.DateTimeField(null=True)),
                ('removed_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'dhurbapp_bloguser',
            },
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 20, 13, 42, 33, 571296)),
        ),
    ]
