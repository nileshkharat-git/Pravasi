from django.urls import path
from . import views
urlpatterns=[
    path('myaccount/<email>',views.myprofile,name='profile'),
    path('booking/',views.booking,name='booking'),
]