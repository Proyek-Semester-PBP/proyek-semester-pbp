# Generated by Django 4.1 on 2022-11-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeem', '0003_remove_voucher_product_voucher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newvoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_voucher_baru', models.TextField()),
                ('desc_voucher_baru', models.TextField()),
            ],
        ),
    ]
