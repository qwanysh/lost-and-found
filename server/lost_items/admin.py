from django.contrib import admin

from lost_items.models import LostItem


@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
