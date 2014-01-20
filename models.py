from django.db import models
from random import randrange


def generate_code():
    """ Borrowed from https://github.com/workmajj/django-unique-random/ """
    CODE_LENGTH = 7
    MAX_TRIES = 1024
    CODE_CHARSET = 'BCDFGHJKMNPQRSTVWXYZ23456789'

    def code_exists(code):
        return False  # TODO Coupon.objects.filter(code=code).exists()

    loop_num = 0
    unique = False
    while not unique:
        if loop_num < MAX_TRIES:
            code = ''
            for i in xrange(CODE_LENGTH):
                code += CODE_CHARSET[randrange(0, len(CODE_CHARSET))]
            if not code_exists(code):
                unique = True
                return code
        else:
            raise ValueError("Couldn't generate a unique code")
            
            
class Coupon(models.Model):
    code = models.CharField(max_length=255, unique=True)
    promotion = models.ForeignKey('coupons.Promotion')
    
    used = models.DateTimeField(blank=True, null=True)
    prize = models.ForeignKey('coupons.Prize', blank=True, null=True)
    redeemer_name = models.CharField(max_length=255, blank=True)
    redeemer_email = models.EmailField(blank=True) #unique=True
    redeemer_phone = models.TextField(blank=True)
    redeemer_address = models.TextField(blank=True)
    redeemer_city = models.TextField(blank=True)
    redeemer_state = models.TextField(blank=True)
    redeemer_zip = models.TextField(blank=True)
    
    
    def __unicode__(self):
        return u'%s' % self.code
        
    def save(self, *args, **kwargs):
        if not self.pk and not self.code:
            self.code = generate_code()
        super(Coupon, self).save(*args, **kwargs)
    
    
class Promotion(models.Model):
    name = models.CharField(max_length=255, unique=True)
    prizes = models.ManyToManyField('coupons.Prize')
    slug = models.SlugField() # if unique=False, then we could run separate promos on the same url, but the coupon code generator would have to change so duplication between promos wouldn't happen
    
    #TODO? active = models.BooleanField()
    
    def bulk_create_codes(self, number):
        codes = []
        for i in range(0, number):
            coupon = self.coupon_set.create()
            codes.append(coupon.code)
        return codes
    
    def __unicode__(self):
        return u'%s' % self.name


class Prize(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % self.name
