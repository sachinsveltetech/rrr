from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.


class UserModelAdmin(BaseUserAdmin):
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','username', 'phone','district','type','is_staff', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('phone','district','type', 'state')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone','district','type', 'password1', 'password2', 'state'),
        }),
    )
    search_fields = ('username',)
    ordering = ('id','username')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
