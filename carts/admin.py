from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
	list_display = ('id', 'listing', 'user')
	list_display_links = ('id', 'listing', 'user')
	list_per_page = 25

# Register your models here.


admin.site.register(Cart)