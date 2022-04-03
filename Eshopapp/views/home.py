from django.shortcuts import render, redirect
from Eshopapp.models import  Categorie, Produit
from django.views import View




class Index(View):

	def post(self, request):
		prod = request.POST.get('produit')
		cart = request.session.get('cart')
		remove = request.POST.get('remove')

		if cart:
			qte = cart.get(prod)

			if qte:
				if remove:

					if qte<=1:
						cart.pop(prod)
					else:
						cart[prod] = qte - 1
				else:
					cart[prod] = qte + 1
			else:
				cart[prod] = 1

		else:
			cart = {}

			cart[prod] = 1
		request.session['cart'] = cart

		print('panier:',request.session['cart'])
			

		return redirect('index')


	def  get(self, request):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		produit = None
		categorie = Categorie.get_all_caregorie()
		catID = request.GET.get('categorie')

		if catID:
			produit = Produit.get_all_product_by_catid(catID)

		else:
			produit = Produit.get_all_product()

		context = {
		'produit':produit,
		'categorie':categorie
		}

		print('votre session ',request.session.get('email'))

		#return render(request, 'order.html')
		return render(request, 'index.html', context)

	
