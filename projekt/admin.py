from .models import Korisnik,Upisi
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
admin.site.register(Upisi)
@admin.register(Korisnik)
class UserAdmin(UserAdmin):
    fieldsets=UserAdmin.fieldsets+(
        ('None',{'fields':('role','status')}),
    )
    add_fieldsets=UserAdmin.add_fieldsets+(
        ('None',{'fields':('role','status')}),
    )