from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cart
from listings.models import Listing
from django.core.paginator import Paginator # Create your views here.

def add(request, listing):
	if request.user.is_authenticated:
		listing_obj = Listing.objects.get(id = listing)
		if listing_obj:
			has_cart = Cart.objects.all().filter(listing = listing, 
											user = request.user.id)
			
			if has_cart:
				messages.error(request, 'You already added this listing to your cart.')
				return redirect('pages:index')
			else:	
				cart = Cart(listing = listing_obj, user = request.user)
				cart.save()
				messages.success(request, 'Successfully added this listing to your cart.')
				return redirect('pages:index')
	else:
		messages.error(request, 'You have to log in.')
		return redirect('accounts:login')
	

def delete(request, listing):
	if request.user.is_authenticated:
		listing_obj = Listing.objects.get(id = listing)
		if listing_obj:
			has_cart = Cart.objects.all().filter(listing = listing, 
											user = request.user.id)
			
			if has_cart:
				has_cart.delete()
				messages.success(request, 'Successfully deleted this Listing')
				return redirect('pages:index')
			else:
				messages.error(request, 'Invalid Credentials')
				return redirect('pages:index')
	else:
		messages.error(request, 'You have to log in.')
		return redirect('accounts:login')