from django.contrib import admin

# Register your models here.
from .models import DeliveryType

@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    pass
