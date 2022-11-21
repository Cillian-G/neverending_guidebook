from django.contrib import admin
from django.contrib.auth.models import User
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_filter = ('subject',)
    search_fields = ('message',)
