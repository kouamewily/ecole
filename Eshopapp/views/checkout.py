from django.shortcuts import render, redirect
from django.views import View
from Eshopapp.models import Produit, Order, Customer



class Checkout(View):
	def post(self, request):
		adresse = request.POST.get('adresse')
		phone = request.POST.get('phone')
		customer = request.session.get('customer')
		cart = request.session.get('cart')
		produit = Produit.get_prodduit_by_id(list(cart.keys()))

		for prod in produit:
			order = Order(customer=Customer(id=customer),
						  produit=prod,
						  prix=prod.prix,
						  add=adresse,
						  phone=phone,
						  qte=cart.get(str(prod.id))
				)
			order.save()

		request.session['cart'] = {}
		return redirect('panier')

		


