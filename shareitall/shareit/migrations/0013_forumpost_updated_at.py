# Generated by Django 5.1.2 on 2024-12-05 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareit', '0012_alter_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]