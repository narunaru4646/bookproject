# Generated by Django 5.1.2 on 2025-06-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
