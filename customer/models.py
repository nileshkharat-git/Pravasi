from django.db import models
from main.models import accounts,Destinations
from django.db.models.signals import post_save
class customer(models.Model):
    """"This model store account general information of user"""
    email=models.ForeignKey(accounts,null=True,on_delete=models.CASCADE)
    place=models.CharField(max_length=255,verbose_name='Place',blank=True,null=True)
    noPassenger=models.IntegerField(verbose_name='No. of Passengers',default=0,blank=True)
    total=models.IntegerField(verbose_name='Total bill',default=0,blank=True)
    DOJ=models.DateField(blank=True,verbose_name='Date of journey',null=True)

# def create_Profile(sender,instance,created,**kwargs):
#     """"This function is able to  automatically create an instance of customer model when user signed up first time"""
#     if created:
#         customer.objects.create(email=instance)
#         print('profile created')
#
# post_save.connect(create_Profile,sender=accounts)