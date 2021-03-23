from django.contrib import admin
from .models import CustomText, Hello, HomePage

admin.site.register(CustomText)
admin.site.register(HomePage)
admin.site.register(Hello)


# Register your models here.
