from django.db import models
from random import randrange
from datetime import date

def generate_code():
    """ 
    Borrowed from https://github.com/workmajj/django-unique-random/ 
    client needed thousands and this worked well.
    i.e. in shell:
        from coupons.models import *
        promotion = Promotion.objects.get(id=1) #id = the promotion id
        promotion.bulk_create_codes(the big number)
        codes = promotion.coupon_set.values_list('code', flat=True)
        # now make a file out of all the codes
        codesFileStream = open('codes.csv', 'w')
        for code in codes:
            codesFileStream.write(code +"\n")
            
        codesFileStream.close() 
    
    """
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


class CouponManager(models.Manager):
    '''
    defines active / usable code user can view/save to if time is before promotion end date 
    and if used is null
    '''
    
    def active(self, **kwargs):
        today = date.today()
        return self.filter(
            models.Q(promotion__end_date__gte=today) | models.Q(promotion__end_date__isnull=True),
            used__isnull=True,
            **kwargs)
            
        
class Coupon(models.Model):
    code = models.CharField(max_length=255, unique=True)
    promotion = models.ForeignKey('coupons.Promotion')
    
    used = models.DateTimeField(blank=True, null=True)
    prize = models.ForeignKey('coupons.Prize', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True) #unique=True
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    promotion_answer = models.CharField(max_length=255, blank=True)
    objects = CouponManager()
    supplier = models.CharField(max_length=255, blank=True)
    fertilizer_used = models.CharField(max_length=200, blank=True, null=True)
    agree = models.BooleanField(blank=True)
    company = models.CharField(max_length=255, blank=True)
    
    
    def __unicode__(self):
        return u'%s' % self.code
        
    def save(self, *args, **kwargs):
        if not self.pk and not self.code:
            self.code = generate_code()
        super(Coupon, self).save(*args, **kwargs)
        
        
class Promotion(models.Model):
    name = models.CharField(max_length=255, unique=True)
    prizes = models.ManyToManyField('coupons.Prize')
    slug = models.SlugField()
    end_date = models.DateTimeField(blank=True, null=True)
    video_embed_code = models.TextField(blank=True)
    promotion_question = models.TextField(blank=True)
    # add super code for testing ???
    
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
