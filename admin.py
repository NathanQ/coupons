from django.contrib import admin

from models import Coupon, Promotion, Prize

class PromotionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    class Meta:
        model = Promotion
        
    
class PrizeAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Prize
        
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Prize, PrizeAdmin)