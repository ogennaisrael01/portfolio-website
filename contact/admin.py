from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date', 'read']
    list_filter = ['read', 'created_date']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['read']
    readonly_fields = ['created_date']

