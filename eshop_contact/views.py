from django.shortcuts import render
from .models import ContactUs

# Create your views here.
from .forms import contactForm
from eshop_settings.models import SiteSetting


def contactPage(request):
    contactform = contactForm(request.POST or None)
    if contactform.is_valid():
        fullname = contactform.cleaned_data.get('fullName')
        email = contactform.cleaned_data.get('email')
        subject = contactform.cleaned_data.get('subject')
        text = contactform.cleaned_data.get('text')

        ContactUs.objects.create(fullName=fullname, email=email, subject=subject, text=text, is_read=False)
        # todo : show user a success message
        contactform = contactForm()

    siteSetting = SiteSetting.objects.first()
    context = {
        "title": "تماس با ما",
        "contact_form": contactform,
        "setting": siteSetting,
    }
    return render(request, "contact_us.html", context)
