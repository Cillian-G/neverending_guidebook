from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Region, Location, Newsletter, Contact, Patron  
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Region)
# @admin.register(Region)
# class RegionAdmin(admin.ModelAdmin):

#     list_display = ('name')


@admin.register(Location)
class LocationAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'region', 'country', 'preview')
    search_fields = ['title', 'content']
    list_filter = ('preview', 'region')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    

@admin.register(Patron)
class PatronAdmin(admin.ModelAdmin):
    list_display = ('user', 'patron_status')
    list_filter = ('patron_status',)
    search_fields = ('user',)

class PatronInline(admin.StackedInline):
    model = Patron

class UserAdmin(BaseUserAdmin):
    inlines = (PatronInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)