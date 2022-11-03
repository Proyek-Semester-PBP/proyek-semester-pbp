from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profpic',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='pics/'),
        ),
    ]
