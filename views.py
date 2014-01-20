from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django import template
from django.shortcuts import render_to_response, get_object_or_404


import csv


from models import Coupon, Promotion

# 1. go to promotion template
# 2. if the coupon code is valid/in database and has not been used, they can proceed to next screen
# 3. Create a CSV file of the coupon redeemers so we can get 'em their awards


def promotion_home(request, promotion_slug):
    #verify the slug
    #display template for people to enter their coupon
    promotion = get_object_or_404(Promotion, slug=promotion_slug)
    return render_to_response("coupons/default.html", params, context_instance=RequestContext(request))


def use_coupon():
    pass
    #if coupon is invalid (not a coupon) or used (has a used date), then stay on page with 'sorry' message.
    #if coupon is valid user can move to form and submit
    #user submits adding used date to coupon


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