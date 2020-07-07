from django.contrib import admin
from .models import accounts,Destinations

class AdminPanel(admin.ModelAdmin):
    list_display = ['email','password','is_admin','is_staff','is_active']

class AdminDestination(admin.ModelAdmin):
    list_display=[
                 'Place',
                 'Address',
                 'Photo',
                 'Description',
                  'RateOfTicket',
                  'inOffer']
            
admin.site.register(accounts,AdminPanel)
admin.site.register(Destinations,AdminDestination)