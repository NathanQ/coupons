from django.conf.urls.defaults import *

# urls is wack

urlpatterns = patterns('coupons.views',
    url(r'^(?P<discipline_slug>\S+)/$', promotion_home, name='promotion_home')
)
