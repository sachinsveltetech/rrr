from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator

#custom usermanager
class UserManager(BaseUserManager):
    def create_user(self, username, phone,district,type, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an user name')

        if not phone:
            raise ValueError('Users must have an phone number')

        user = self.model(
            username=username,
            phone=phone,
            district=district,
            type=type,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone,district,type, password=None):
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
            district=district,
            type=type
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custom user Model
class User(AbstractBaseUser):
    ACCOUNT_TYPE = [
        ('SUPER_USER', 'SUPER_USER'),
        ('ADMIN', 'ADMIN'),        
        ('TSP', 'TSP'),
        ('USER', 'USER'),
    ]
    mobile_number_errors = {'required': 'Mobile number is required',
                            'invalid': 'Enter a valid 10 digit mobile number' +
                            'without spaces, + or isd code.'}
    mobile_regex_validator = RegexValidator(regex=r"^[6-9]\d{9}$",
                                             message="Invalid phone number")
    username=models.CharField(max_length=255,unique=True)
    phone = models.CharField(
        verbose_name='Mobile Number',
        max_length=12,
        unique=True,
        validators=[mobile_regex_validator],blank=False, null=False,error_messages=mobile_number_errors)
    district = models.CharField(max_length=255)
    type = models.CharField(choices=ACCOUNT_TYPE, max_length=255, default='USER')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone','district','type']

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
