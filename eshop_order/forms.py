from django import forms


class OrderForm(forms.Form):
    productID = forms.IntegerField(widget=forms.HiddenInput())

    count = forms.IntegerField(widget=forms.NumberInput(), initial=1)
