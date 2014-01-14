from django.http import HttpResponse
import csv

from models import Coupon, Promotion
# 1. if the coupon code is valid/in database and has not been used, they can proceed to next screen
# 2. Create a CSV file of the coupon redeemers so we can get 'em their awards

def use_coupon():

def export_coupon_redeemers(request):
    
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename="coupon_redeemers.csv"'

    writer = csv.writer(response)
    writer.writerow(['Promotion', 'Code', 'Award', 'First Name', 'Last Name', 
                    'Email', 'Phone', 'Address', 'State', 'Zip', ])

    enrollments = Enrollment.objects.all()
    for enrollment in enrollments:
        writer.writerow([
            coupons.promotion,
            coupons.code,
            coupons.promotion_award,
            coupons.first_name,
            coupons.last_name,
            coupons.email,
            coupons.phone,
            coupons.address,
            coupons.state,
            coupons.zip,
        ])

    return response