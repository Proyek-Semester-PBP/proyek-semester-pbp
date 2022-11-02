# Generated by Django 4.1 on 2022-11-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_voucher', models.TextField()),
                ('title_voucher', models.TextField()),
                ('harga_poin', models.IntegerField()),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]
