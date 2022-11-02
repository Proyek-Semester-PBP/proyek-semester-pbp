from django.db.models import fields
from redeem.models import Newvoucher
from django.forms import ModelForm


class VoucherForm(ModelForm):

 class Meta:
        model = Newvoucher
        fields = ('nama_voucher_baru', 'desc_voucher_baru')