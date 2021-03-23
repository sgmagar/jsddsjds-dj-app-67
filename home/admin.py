from django.contrib import admin
from .models import CustomText


@admin.register(CustomText)
class CusomTextAdmin(admin.ModelAdmin):
    pass


# Register your models here.
