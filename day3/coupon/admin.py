from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'use_from', 'use_to', 'amount', 'activate']
    list_filter = ['activate', 'use_from', 'use_to']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
