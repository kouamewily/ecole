from django.shortcuts import render, redirect
from django.views import View
from Eshopapp.models import Produit



class Cart(View):
	def get(self, request):

		ids = list(request.session.get('cart').keys())

		produits = Produit.get_prodduit_by_id(ids)
		return render(request,'cart.html',{'produits':produits})


