from django.urls import path
from .views import *

urlpatterns = [
    path('sv/',signup_view,name='signup_view_url'),
    path('lv/',login_view,name='login_view_url'),
    path('lo/',logout_view,name='logout_view_url')
]