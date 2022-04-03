from django.shortcuts import render, redirect
from django.views import View
from Eshopapp.models import Produit, Order, Customer
from Eshopapp.middlewares.auth import auth_middleware
#from django.utils.decorators import method_decorator

class OrderView(View):

	
	def get(self, request):
		
		orders = Order.get_orders_by_customer()
		orders = orders.reverse()
	
		return render(request, 'order.html', {'order':orders})




		


