from django.contrib import admin
from .models import PatronUpgrade


@admin.register(PatronUpgrade)
class PatronUpgradeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date', 'order_number')
    list_filter = ('date',)
    search_fields = ('email', 'order_number')