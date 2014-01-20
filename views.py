from django.http import HttpResponse
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django import template
from django.shortcuts import render_to_response, get_object_or_404

import csv

from models import Coupon, Promotion
from .forms import CouponCodeForm, CouponForm

# 1. go to promotion template and submit code
# 2. if the coupon code is valid/in database and has not been used, they can proceed to next screen,
#   the coupon code.
# 3. fill out form, use code, and go to thank you page.
# 4. Admins will be able to create a CSV file of the coupon redeemers so they can get 'em their awards


def promotion_home(request):
    #verify the slug
    #display template for people to enter their coupon
    form = CouponCodeForm(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data.get('code')
        return redirect(reverse('coupon_view', args=[code])) # to coupon code view for this code
        
    return render_to_response("coupons/home.html", {'form':form}, context_instance=RequestContext(request))

    #if coupon is invalid (not a coupon) or used (has a used date), then stay on page with 'sorry' message.
    #if coupon is valid user can move to form and submit
    #user submits adding used date to coupon
    
def coupon_view(request, code):
    coupon = get_object_or_404(Coupon, code=code, used__isnull=True)
    form = CouponForm(request.POST or None, instance=coupon)
    if form.is_valid():
        coupon = form.save()
        # TODO redirect to thanks

    return render_to_response("coupons/promo.html", params, context_instance=RequestContext(request))

def export_coupon_redeemers(request):
    
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename="coupon_redeemers.csv"'

    writer = csv.writer(response)
    writer.writerow(['Promotion', 'Code', 'Award', 'First Name', 'Last Name', 
                    'Email', 'Phone', 'Address', 'State', 'Zip', ])

    coupons = Coupon.objects.all()
    for coupon in coupons:
        writer.writerow([
            coupons.promotion,
            coupons.code,
            coupons.prize,
            coupons.redeemer_name,
            coupons.email,
            coupons.phone,
            coupons.address,
            coupons.state,
            coupons.zip,
        ])

    return response