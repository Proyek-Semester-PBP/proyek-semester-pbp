from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0005_alter_profile_profpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profpic',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='pics/'),
        ),
    ]
