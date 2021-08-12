from django.urls import path
from .views import *

urlpatterns = [
    path('logout', log_out),
    path('login', loginPage),
    path('register', registerPage),
    path('panel', user_panel),
    path('panel/edit-profile', edit_profile),
]
