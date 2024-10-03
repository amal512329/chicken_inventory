from django.contrib import admin
from .models import Inventory
# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('chickens', 'legs', 'wings', 'flesh') 