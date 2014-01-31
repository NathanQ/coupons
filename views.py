from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
import datetime
from datetime import date
from django import template
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.mail import EmailMultiAlternatives

import csv

from models import Coupon, Promotion
from .forms import CouponCodeForm, CouponForm

# 1. go to promotion template and submit code
# 2. if the coupon code is valid/in database and has not been used, they can proceed to next screen,
#   the coupon code.
# 3. fill out form, use code, and go to thank you page.
# 4. Admins will be able to create a CSV file of the coupon redeemers so they can get 'em their awards


def promotion_home(request):
    '''
    1.  verify the slug
    2.  display template for people to enter their coupon
    3.  on form submission (see forms CouponCodeForm) redirect to coupon view.
    '''
    
    form = CouponCodeForm(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data.get('code')
        return redirect(reverse('coupon_view', args=[code])) # to coupon code view for this code
        
    return render_to_response("coupons/home.html", {'form':form}, context_instance=RequestContext(request))

    
def coupon_view(request, code):
    '''
    1.  if coupon is invalid (not a coupon) or used (has a used date), 
        then stay on page with 'sorry' message - that fx is in forms.
    2.  if coupon is valid user can view page
    3.  on form submission (see forms CouponForm), form saves, emails user and redirects to django page
    '''
    
    coupon = get_object_or_404(Coupon, code=code, used__isnull=True)
    form = CouponForm(request.POST or None, instance=coupon)
    print form
    if form.is_valid():
        
        email = form.cleaned_data['email']
        html_template = 'coupons/thanks_email.html'
        text_template = 'coupons/thanks_email.txt'
        html_rendered = render_to_string(html_template, request.GET)
        text_rendered = render_to_string(text_template, request.GET)
        subject = 'You did it!'
        from_email = 'you@mail.com'
        to_email = [email]
        msg = EmailMultiAlternatives(subject, text_rendered, from_email, to_email)
        msg.attach_alternative(html_rendered, 'text/html')
        msg.send()
        coupon = form.save()
        return redirect('/thank-you/')

    return render_to_response("coupons/promo.html", {'form':form,'coupon':coupon}, context_instance=RequestContext(request))
    
@user_passes_test(lambda u: u.is_staff, login_url="/admin/")
def export_coupon_redeemers(request):
    '''
    1.  Must be logged in.
    2.  go to /admin/coupons/coupon/enroll to download the csv.
    '''
    
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export_coupon_redeemers.csv"'

    writer = csv.writer(response)
    writer.writerow(['Promotion', 'Code', 'Award', 'Name', 'Company',
                    'Address', 'City', 'State', 'Zip', 'Email', 'Phone', 'Acres', 'Fertilizers'  ])

    coupons = Coupon.objects.all()
    for coupon in coupons:
        writer.writerow([
            coupon.promotion,
            coupon.code,
            coupon.prize,
            coupon.name,
            coupon.company,
            coupon.address,
            coupon.state,
            coupon.city,
            coupon.zip,
            coupon.email,
            coupon.phone,
            coupon.promotion_answer,
            coupon.fertilizer_used,
        ])

    return response