from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class mymanager(BaseUserManager):
    """"This is profile manager model"""
    def create_user(self,email,username,password=None):
        """"this function create simple user for an application"""
        if not email:
            raise ValueError('Email not provided')

        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,password):
        """"this function create super(owner) user for an application"""
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)
        return user
class accounts(AbstractBaseUser):
    """"This is custom user model for website account"""
    email=models.CharField(max_length=60,primary_key=True,verbose_name="Email")
    username=models.CharField(max_length=255,unique=True)
    profilePic=models.ImageField(blank=True,null=True,upload_to='profile')
    date_joined=models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username',]

    objects=mymanager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Destinations(models.Model):
    """"This model is using for storing destinations."""
    Place=models.CharField(max_length=100,primary_key=True)
    Address=models.CharField(max_length=100)
    Photo=models.ImageField(blank=True,null=True,upload_to='destination')
    Description=models.TextField(max_length=150)
    RateOfTicket=models.FloatField(verbose_name='Ticket rate',null=True)
    inOffer=models.BooleanField(verbose_name='Offer',null=True)

    def __str__(self):
        return self.Place
