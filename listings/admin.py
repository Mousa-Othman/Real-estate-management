from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'address', 
					'zipcode', 'price', 'is_published', 
					'square_feet', 'list_date', 'realtor')
	list_display_links = ('id', 'title')
	list_filter = ('realtor', 'is_published')
	search_fields = ('title', 'address', 'zipcode', 'realtor')
	list_editable = ('is_published',)
	list_per_page = 25
	
# Register your models here.

admin.site.register(Listing, ListingAdmin)