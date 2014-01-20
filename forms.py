from django import forms
from django.forms import ModelForm
from models import Coupon, Promotion

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon

    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)