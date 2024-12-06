# Generated by Django 5.1.2 on 2024-12-05 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareit', '0007_product_image_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='contact_info',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
