from django import forms


class AddCouponForm(forms.Form):
    code = forms.CharField(label='쿠폰코드 입력')
