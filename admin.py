from django.contrib import admin
from django.conf.urls.defaults import patterns, url

from models import Coupon, Promotion, Prize
from views import export_coupon_redeemers

class PromotionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    class Meta:
        model = Promotion
        
class PrizeAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Prize


class CouponAdmin(admin.ModelAdmin):
    
    list_display = ('promotion', 'prize', 'name', 'company',
                    'email', 'phone', 'supplier', 'used')
                   
    list_filter = ['promotion', 'used']
    
    def queryset(self, request):
        return super(CouponAdmin, self).queryset(request).select_related('agree')
    
    def get_urls(self):
        old_urls = super(CouponAdmin, self).get_urls()
        new_urls = patterns('',
            url(r'^export/$', export_coupon_redeemers, name='export_coupon_redeemers'),
        )
        return new_urls + old_urls
        
    #no button to export, just go to /export
        
    show_firm_url = ['get_urls']

    class Meta:
        model = Coupon

admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(Coupon, CouponAdmin)