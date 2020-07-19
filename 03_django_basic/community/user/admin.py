from django.contrib import admin
from .models import UserCustom

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(UserCustom, UserAdmin)
