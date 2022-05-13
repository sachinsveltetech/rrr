# from tkinter import CASCADE
# from sre_parse import State
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator
from common.models import Tsp,District,State
from .utils import ACCOUNT_TYPE


#custom usermanager
class UserManager(BaseUserManager):
    def create_user(self, username, phone ,email,password=None, password2=None,**extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an user name')

        if not phone:
            raise ValueError('Users must have an phone number')
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            phone=phone,
            email=email,
            
           
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone,type, password=None,**extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if password is None:
            raise ValueError('Password should not be none')
        user = self.create_user(
            username=username,
            phone=phone,
            password=password,            
            type=type,
            **extra_fields,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custom user Model
class User(AbstractBaseUser):
    
    mobile_number_errors = {'required': 'Mobile number is required',
                            'invalid': 'Enter a valid 10 digit mobile number' +
                            'without spaces, + or isd code.'}
    mobile_regex_validator = RegexValidator(regex=r"^[6-9]\d{9}$",
                                             message="Invalid phone number")
    username=models.CharField(max_length=255,unique=True)
    email=models.EmailField(max_length=250,unique=True,blank=True,null=True)    
    phone = models.CharField(
        verbose_name='Mobile Number',
        max_length=12,
        unique=True,
        validators=[mobile_regex_validator],blank=False, null=False,error_messages=mobile_number_errors)
    district = models.ForeignKey(District,on_delete=models.CASCADE,blank=True,null=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(choices=ACCOUNT_TYPE, max_length=255, default='USER')
    tsp_company=models.ForeignKey(Tsp,on_delete=models.CASCADE,blank=True,null=True, related_name="user_tsp_companies")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','type',]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
    