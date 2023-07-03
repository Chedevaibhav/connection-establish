from django.contrib import admin
from .models import Dbmodel

# Register your models here.


class Dbadmin(admin.ModelAdmin):
    list_display = ['name','age','city','employee','n1','behavior']


admin.site.register(Dbmodel,Dbadmin)
