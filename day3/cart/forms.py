from django import forms
class AddProductForm(forms.Form):#제품 추가할때 갯수를 넣게한다.
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)