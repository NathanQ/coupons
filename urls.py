from django.conf.urls.defaults import *


urlpatterns = patterns('coupons.views',
    url(r'^$', 'promotion_home', name='promotion_home'),
    url(r'^(?P<code>\S+)/$', 'coupon_view', name='coupon_view')
)
