from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import *
from datetime import datetime
from realtors.models import Realtor
# Create your views here.

def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published = True)
	paginator = Paginator(listings, 6)
	page_number = request.GET.get('page')
	page_listings = paginator.get_page(page_number)
	context = {
		'listings': page_listings
	}
	return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
	listing = get_object_or_404(Listing, id = listing_id)
	context = {
		'listing': listing,
	}
	return render(request, 'listings/listing.html', context)

def search(request):
	queryset_list = Listing.objects.order_by('-list_date')
	
	# Keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains = keywords)

	# City
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			queryset_list = queryset_list.filter(city__iexact = city)

	# State
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
			queryset_list = queryset_list.filter(state__iexact = state)

	# Bedroom
	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		if bedrooms:
			queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)

	# Price
	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__lte = price)
	context = {
		'listings' : queryset_list,
		'state_choices' : STATE_CHOICES,
		'price_choices' : PRICE_CHOICES,
		'bedroom_choices' : BEDROOM_CHOICES,
		'values_back': request.GET
		
	}
	return render(request, 'listings/search.html', context)
def add(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			context = {
				'state_choices' : STATE_CHOICES,
				'price_choices' : PRICE_CHOICES,
				'bedroom_choices' : BEDROOM_CHOICES
			}
			return render(request, 'listings/add_listing.html', context)
		else:
			# title 		= request.POST['title']
			# address 	= request.POST['address']
			# city 		= request.POST['city']
			# state 		= request.POST['state']
			# zipcode 	= request.POST['zipcode']
			# description = request.POST['description']
			# price 		= request.POST['price']
			# bedrooms 	= request.POST['bedrooms']
			# bathrooms 	= request.POST['bathrooms']
			# garages 	= request.POST['garages']
			# sqroot 		= request.POST['sqroot']
			# lotsize 	= request.POST['lotsize']
			# mainphoto 	= request.POST['mainphoto']
			# photo_1 = request.POST['photo1']
			# photo_2 = request.POST['photo2']
			# photo_3 = request.POST['photo3']
			# photo_4 = request.POST['photo4']
			# photo_5 = request.POST['photo5']

			# listing = Listing(realtor = realtor, title = title, address = address,
			# 				  city = city, state = state, zipcode = zipcode, description = description,
			# 				  price = price, bedrooms = bedrooms, bathrooms = bathrooms,
			# 				  garage = garages, square_feet = sqroot, lot_size = lotsize,
			# 				  mainphoto = mainphoto, photo_1 = photo_1, photo_2 = photo_2,
			# 				  photo_3 = photo_3, photo_4 = photo_4,	photo_5 = photo_5,
			# 				  is_published = False,	list_date = datetime.now)

			# listing.save()
			# messages.success(request, 'Successfully added your listing.')
			# return redirect('accounts:dashboard')
			pass
	else:
		messages.error(request, 'You have to login.')
		return redirect('accounts:login')
