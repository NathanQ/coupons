from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm
from models import Coupon, Promotion


class CouponCodeForm(forms.Form):
    code = forms.CharField()

    def clean_code(self):
        code = self.cleaned_data.get('code')
        valid_code = Coupon.objects.filter(used__isnull=True, code=code).exists()
        if not valid_code:
            raise forms.ValidationError("This promotion code has either been used or is invalid. If you'd like to watch the video, go to textbooksop.com/growing-knowledge")
        return code


class CouponForm(forms.ModelForm):
    
    class Meta:
        model = Coupon
    
    fields = ('name', 'code', 'used', 'promotion', 'company', 'address', 'city', 'state', 'zip', 'email', 'phone', 'prize', 'supplier', 'promotion_answer', 'fertilizer_used', 'agree' )
    
    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        self.fields['promotion_answer'].label = self.instance.promotion.promotion_question