#coding: utf8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profiles.models import UserProfile

# Register your models here.
# admin.site.register(UserProfile)

class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name = 'Profile do Usuário'
    verbose_name_plural = 'Profile do Usuário'

class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInLine, )

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)