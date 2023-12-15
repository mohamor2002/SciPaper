from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import BasicUser


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = BasicUser
    can_delete = True
    verbose_name_plural = "users"
    verbose_name = "user"

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)