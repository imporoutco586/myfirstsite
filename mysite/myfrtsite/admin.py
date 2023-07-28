from django.contrib import admin
from .models import Article , SiteUser
# Register your models here.

admin.site.register(Article)

class SiteUserAdmin(admin.ModelAdmin):
    list_display = ['name','gender']
    list_filter = ['name']
    list_per_page = 2
    list_display_links = ['name']
admin.site.register(SiteUser,SiteUserAdmin)
