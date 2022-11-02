# Generated by Django 4.1 on 2022-11-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_recommendeditem_bookmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=150)),
                ('user', models.CharField(max_length=150)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
