from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User


# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("/")
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        userName = login_form.cleaned_data.get("username")
        passWord = login_form.cleaned_data.get("password")
        user = authenticate(request, username=userName, password=passWord)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error('username', 'اطلاعات وارد شده صحیح نیست')
    context = {
        "title": "ورود",
        "form": login_form,
    }
    return render(request, "account/login.html", context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("/")
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        userName = register_form.cleaned_data.get("username")
        Email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        password2 = register_form.cleaned_data.get("password2")

        User.objects.create_user(username=userName, email=Email, password=password)
        return redirect("/login")
    context = {
        "title": "ثبت نام",
        "form": register_form
    }
    return render(request, "account/register.html", context)


def log_out(request):
    logout(request)
    return redirect('/')


@login_required(login_url="/login")
def user_panel(request):
    context = {
        "title": "پنل کاربری",
    }
    return render(request, "account/user_panel.html", context)


@login_required(login_url="/login")
def edit_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()

    editForm = EditForm(request.POST or None, initial={"first_name": user.first_name, "last_name": user.last_name})

    if editForm.is_valid():
        first_ame = editForm.cleaned_data.get("first_name")
        last_name = editForm.cleaned_data.get("last_name")
        user.firstName = first_ame
        user.lastName = last_name
        user.save()

    context = {
        "title": "ویرایش اطلاعات",
        "edit_form":editForm,
    }
    return render(request, "account/edit_profile.html", context)


def sidebar_panel(request):
    return render(request, "account/sidebar_panel.html")
