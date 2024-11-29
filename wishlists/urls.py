from django.urls import path
from . import views

app_name = 'wishlists'

urlpatterns = [
	path('add/<int:listing>', views.add, name= 'add'),
	path('delete/<int:listing>', views.delete, name= 'delete'),
] 
