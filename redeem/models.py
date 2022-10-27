from django.db import models

class Voucher(models.Model):
    jenis_voucher = models.TextField()
    title_voucher =  models.TextField()
    produk_voucher = models.TextField()
    harga_poin = models.IntegerField()
    deskripsi = models.TextField()
    
# Create your models here.
