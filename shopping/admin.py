from django.contrib import admin
from shopping.models import RecommendedItem, RecommendedVendor

# Register your models here.
admin.site.register(RecommendedItem)
admin.site.register(RecommendedVendor)
