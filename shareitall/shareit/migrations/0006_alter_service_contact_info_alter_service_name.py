# Generated by Django 5.1.2 on 2024-12-04 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareit', '0005_remove_product_created_at_alter_listing_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='contact_info',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]