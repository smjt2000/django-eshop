from django import forms


class contactForm(forms.Form):
    fullName = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "نام و نام خانواذگی", "class": "form-control"
    }), label="نام و نام خانوادگی", max_length=45)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "ایمیل", "class": "form-control"
    }), label="ایمیل", max_length=100)

    subject = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "موضوع پیام", "class": "form-control"
    }), label="موضوع پیام", max_length=200)

    text = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control", "placeholder": "متن پیام", "rows": 10
    }), label="متن پیام")
