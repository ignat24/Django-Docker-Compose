from .models import CustomUser
from django.contrib import admin
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email'] # add fields as you want

admin.site.register(CustomUser, CustomUserAdmin)