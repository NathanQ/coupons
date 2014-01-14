from django.contrib import admin

from models import Coupon, Promotion


class CouponAdmin(admin.ModelAdmin):
    list_display = ('promotion', 'promotion_award',
    'redeemer_last_name', 'redeemer_first_name', )
    
    class Meta:
        model = Coupon

class PromotionAdmin(admin.ModelAdmin):
    #will need to be able to add promotions, the award(s), and the promotion's coupon sets.
    list_display = ('promotion',)
    
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Promotion, PromotionAdmin)