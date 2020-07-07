from django.contrib import admin
from .models import customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email','place','noPassenger','total','DOJ']

admin.site.register(customer,CustomerAdmin)
