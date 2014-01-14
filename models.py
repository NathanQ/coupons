from django.db import models

'''
*** App description ***

1.  the user will either go to site.com/promotion?coupon_code from link
    and code will prepopulate the value of the code of the form
    or they go to site.com/promotion and enter the coupon code

2.  if the coupon code is valid/in database and has not been used, 
    they can proceed to next screen
    they will fill out a form, choose award and submit
    submitting form will use the coupon

3.  we will at some point download all the entries in a csv file to 
    send 'em their award.

'''

class Coupon(models.Model):
    code = models.CharField(max_length=255, unique=True)
    used = models.DateTimeField(blank=True)   
    redeemer_first_name = models.CharField(max_length=255, blank=True)
    redeemer_last_name = models.CharField(max_length=255, blank=True)
    redeemer_email = models.EmailField(blank=True)
    redeemer_phone = models.TextField(blank=True)
    redeemer_address = models.TextField(blank=True)
    redeemer_city = models.TextField(blank=True)
    redeemer_state = models.TextField(blank=True)
    redeemer_zip = models.TextField(blank=True)
    promotion = models.ForeignKey('Promotion')
    
    #   we can move on if the a code is valid. how do I do that?
    #   if coupon is invalid or used, then stay on page with 'sorry' message. 
    #   page has to show, but next step will not be available.
    
    def __unicode__(self):
        return u'%s' % self.title
    
class Promotion(models.Model):
    promotion = models.CharField(max_length=255, unique=True)
    promotion_award = models.CharField(max_length=255, unique=True) #oops, this needs to be a set of choices
    #slug should be /promotion?couponcode
    #template - is can this be dynamically chosen when adding a promotion?
    #should we have a from and through date for promotion time frame?
    #each promotion will have a coupon code set. do I make em here or upload?
    
    def __unicode__(self):
        return u'%s' % self.title
     
