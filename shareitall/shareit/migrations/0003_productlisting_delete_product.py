# Generated by Django 5.1.2 on 2024-12-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareit', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
