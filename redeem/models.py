from django.db import models

class Voucher(models.Model):
    jenis_voucher = models.TextField()
    title_voucher =  models.TextField()
    harga_poin = models.IntegerField()
    deskripsi = models.TextField()

    
class Newvoucher(models.Model):
    nama_voucher_baru = models.TextField()
    desc_voucher_baru = models.TextField()