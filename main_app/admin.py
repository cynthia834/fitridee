from django.contrib import admin

from main_app.models import Bicycle, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Bicycle)
