# Generated by Django 4.1 on 2022-10-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profpic',
            field=models.URLField(default=0, max_length=500, null=True),
        ),
    ]