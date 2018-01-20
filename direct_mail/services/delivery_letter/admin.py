from django.contrib import admin

# Register your models here.
from .models import DeliveryType
from .models import Letter

@admin.register(DeliveryType)
class DeliveryTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    pass
