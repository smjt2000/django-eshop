from django import forms
from django.contrib.auth.models import User


class EditForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "نام خود را وارد کنید", "class": "form-control",
    }), label="نام")

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "نام خانوادگی خود را وارد کنید", "class": "form-control",
    }), label="نام خانوادگی")


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "نام کاربری را وارد کنید",
    }), label="نام کاربری")

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "کلمه عبور را وارد کنید",
    }), label="کلمه عبور")

    def clean_username(self):
        user_name = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=user_name).exists()
        if not user_exists:
            raise forms.ValidationError("نام کاربری وارد شده صحیح نمیباشد")
        return user_name


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "نام کاربری را وارد کنید",
    }), label="نام کاریری")

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "ایمیل خود را وارد کنید",
    }), label="ایمیل")

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "کلمه عبور را وارد کنید",
    }), label="کلمه عبور", min_length=6)

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "کلمه عبور را تایید کنید",
    }), label="تایید کلمه عبور", min_length=6)

    def clean_username(self):
        user_name = self.cleaned_data.get("username")
        user_exists = User.objects.filter(username=user_name).exists()
        if user_exists:
            raise forms.ValidationError("کاربری با نام کاریری وارد شده وجود دارد")
        return user_name

    def clean_email(self):
        Email = self.cleaned_data.get("email")
        email_exists = User.objects.filter(email=Email).exists()
        if email_exists:
            raise forms.ValidationError("کاربری با ایمیل وارد شده وجود دارد")

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("کلمه عبور و تکرار آن مشابه نیستند")
        return password
