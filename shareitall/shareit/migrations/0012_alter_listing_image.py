# Generated by Django 5.1.2 on 2024-12-05 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareit', '0011_alter_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
    ]
