from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from carts.models import Cart
from wishlists.models import Wishlist

from django.contrib.auth.hashers import make_password

# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username= username, password= password)
		if user:
			auth.login(request, user)
			messages.success(request, 'You are now logged in.')
			return redirect('accounts:dashboard')
		else:
			messages.error(request, 'Invalid Credentials.')
			return redirect('accounts:login')
	else:
		return render(request, 'accounts/login.html')

def register(request):
	if request.method == 'POST':
		data = {
			'first_name': request.POST['first_name'],
			'last_name': request.POST['last_name'],
			'username': request.POST['username'],
			'email': request.POST['email'],
			'password': request.POST['password'],
			'password2': request.POST['password2'],
		}
		# Simple validation for password
		if data['password'] == data['password2']:
			# Simple validation for username
			if User.objects.filter(username= data['username']).exists():
				messages.error(request, 'Username is exists.')
				return redirect('accounts:register')
			else:
				# Simple validation for username
				if User.objects.filter(email= data['email']).exists():
					messages.error(request, 'Email is exists.')
					return redirect('accounts:register')
				else:
					user = User.objects.create_user(
						first_name= data['first_name'],
						last_name= data['last_name'],
						username= data['username'],
						email= data['email'],
						password= data['password'],
						)
					user.save()
					messages.success(request, 'Successfully registered, Login here.')
					return redirect('accounts:login')

		else:
			messages.error(request, 'Two passwords must matches.')
			return redirect('accounts:register')
	else:
		return render(request, 'accounts/register.html')


def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request, 'Successfully logged out.')
		return redirect('pages:index')


def dashboard(request):
	contacts = Contact.objects.order_by('-contact_date').filter(user_id= request.user.id)
	carts = Cart.objects.all().filter(user_id= request.user.id)
	wishlists = Wishlist.objects.order_by('-date').filter(user_id= request.user.id)
	context = {
		'contacts': contacts,
		'carts': carts,
		'wishlists': wishlists
	}
	return render(request, 'accounts/dashboard.html', context)

def editprofile(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			return render(request, 'accounts/editprofile.html')
		else:
			username = request.POST['username']
			email = request.POST['email']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			password1 = request.POST['password1']
			password2 = request.POST['password2']

			if password1 == password2:
				request.user.username = username
				request.user.email = email
				request.user.first_name = first_name
				request.user.last_name = last_name
				if password1 == '' and password2 == '':
					pass
				else:
					request.user.password = make_password(password1)
				request.user.save()
				messages.success(request, 'Profile Edited Successfully.')
				return redirect('accounts:editprofile')
			else:
				messages.error(request, 'Password and Password Confirmation must be the same.')
				return redirect('accounts:editprofile')
	else:
		messages.error(request, 'You have to login.')
		return redirect('accounts:login')



	
