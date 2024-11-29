from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Contact
from django.core.paginator import Paginator

# Create your views here.

def contact(request):
	if request.method == 'POST':
		listing_title	= request.POST['listing']
		listing_id 		= request.POST['listing_id']
		name 			= request.POST['name']
		email			= request.POST['email']
		phone			= request.POST['phone']
		message			= request.POST['message']
		user_id			= request.POST['user_id']
		realtor_email	= request.POST['realtor_email']

		if request.user.is_authenticated:
			has_contacted = Contact.objects.all().filter(listing_id = listing_id, user_id = request.user.id)
			if has_contacted:
				messages.error(request, "You have already make an inquery")
				redirect('/listings/' + listing_id)
		contact = Contact(listing_title = listing_title,
						  listing_id = listing_id,
						  name = name,
						  email = email,
						  phone = phone,
						  message = message,
						  user_id = user_id)
		contact.save()
		messages.success(request, 'Thanks for your supportive message')
		return redirect('/listings/' + listing_id)