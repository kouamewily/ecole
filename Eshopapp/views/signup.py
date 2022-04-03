from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from Eshopapp.models import  Customer
from django.views import View



class SignUp(View):

	def get(self, request):
		return render(request,'signup.html')

	def post(self, request):
		postData = request.POST
		nom = postData.get('nom')
		email = postData.get('email')
		phone = postData.get('phone')
		password = postData.get('password')

		value = {
		'nom':nom,
		'email':email,
		'phone':phone
		}

		error_msg =None

		customer = Customer(nom=nom, email=email, phone=phone, password=password)

		error_msg = self.ValidateCustomer(customer)

		if not error_msg:
			print(nom, email, phone, password)

			customer.password = make_password(customer.password)
			customer.register()
			return redirect('index')
		else:
			context = {
			'error':error_msg,
			'values':value
			}

			return render(request, 'signup.html', context)


	def ValidateCustomer(self,customer):
		error_msg = None
		if (not customer.nom):
				error_msg = 'le nom est obligatoire'

		elif len(customer.nom)<5:
			error_msg = 'le nom doit depasser 5 caracteres'


		if (not customer.phone):
				error_msg = 'le numero de telephone est obligatoire'

		elif len(customer.phone)<10:
				error_msg = 'le num doit depasser 10 chiffre'

		if (not customer.password):
			error_msg = 'le MP est obligatoire'
			
		elif  len(customer.password)<6:
				error_msg = 'le MP doit depasser 6 chiffre'

		elif customer.isExist():
			error_msg = 'cette adresse email est deja utilisé'

		return error_msg


