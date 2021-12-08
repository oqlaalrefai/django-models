from django.contrib import admin
from .models import snack
# Register your models here.
admin.site.register(snack)

class AdminSnack(admin.ModelAdmin):
    list_display = ['name','purchaser']
    