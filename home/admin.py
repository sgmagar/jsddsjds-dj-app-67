from django.contrib import admin
from .models import CustomText, HomePage

@admin.register(CustomText)
class CustomTextAdmin(admin.ModelAdmin):
  pass

admin.site.register(HomePage)


# Register your models here.
