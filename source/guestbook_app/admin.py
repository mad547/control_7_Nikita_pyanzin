from django.contrib import admin
from guestbook_app.models import Entry

# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'status', 'created_at']
    list_filter = ['status',]
    search_fields = ['name', 'email']


admin.site.register(Entry, EntryAdmin)