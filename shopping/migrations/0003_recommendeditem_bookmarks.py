# Generated by Django 4.1 on 2022-10-31 11:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0002_recommendeditem_image_recommendedvendor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendeditem',
            name='bookmarks',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]