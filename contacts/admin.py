from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'listing_title', 'listing_id', 
					'name', 'email', 'phone', 
					'contact_date', 'user_id')
	list_display_links = ('id', 'listing_title', 'name')
	search_fields = ('listing_title', 'name', 'email')
	list_per_page = 25

admin.site.register(Contact, ContactAdmin)
