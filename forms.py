from django import forms
from django.forms import ModelForm
from models import Coupon, Promotion


class CouponCodeForm(forms.Form):
    code = forms.CharField()

    def clean_code(self):
        code = self.cleaned_data.get('code')
        valid_code = Coupon.objects.filter(used__isnull=True, code=code).exists()
        if not valid_code:
            raise forms.ValidationError("Invalid coupon code")
        return code


class CouponForm(forms.ModelForm):
    fields = ('redeemer_name', 'redeemer_answer', )

    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        self.fields['promotion_answer'].label = self.instance.promotion.promotion_question

    class Meta:
        model = Coupon