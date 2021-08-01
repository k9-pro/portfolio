from django.contrib import admin
from .models import Site, Location, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# accounts.apps.AccountsConfig


class ProfileInline(admin.StackedInline) :
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
# Register your models here.

class CustomizedUserAdmin(UserAdmin) :
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(Site)
admin.site.register(Location)
admin.site.register(User, CustomizedUserAdmin)