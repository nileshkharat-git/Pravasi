from django.urls import path,include
from . import views
import customer.urls
urlpatterns=[
    path('signup/',views.userSignup,name='signup'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userlogout),
    path('profile/',include(customer.urls))
]