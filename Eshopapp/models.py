from django.db import models

import datetime 





class Categorie(models.Model):
	nom = models.CharField(max_length=100)

	@staticmethod
	def get_all_caregorie():
		return Categorie.objects.all()


	def __str__(self):
		return self.nom

class Produit(models.Model):
	nom = models.CharField(max_length=50)
	prix = models.IntegerField(default=0)
	cat = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
	description = models.CharField(max_length=200, default='')
	image = models.ImageField(upload_to='produit//%Y/%m/%d/')

	def __str__(self):
		return self.nom

	@staticmethod
	def get_prodduit_by_id(ids):
		return Produit.objects.filter(id__in=ids)


	@staticmethod
	def get_all_product():
		return Produit.objects.all()

	@staticmethod
	def get_all_product_by_catid(cat_id):

		if cat_id:
			return Produit.objects.filter(cat=cat_id)

		else:
			return Produit.objects.all()


class Customer(models.Model):
	nom = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	email = models.EmailField()
	password = models.CharField(max_length=200)

	def register(self):
		return self.save()

	@staticmethod
	def get_customer_by_email(email):
		try:
			return Customer.objects.get(email=email)
		except:
			return False
			
		


	def isExist(self):
		if Customer.objects.filter(email=self.email):
			return True

		return False


	def __str__(self):
		return self.nom

class Order(models.Model):
	produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	qte = models.IntegerField(default=1)
	prix = models.IntegerField()
	add = models.CharField(max_length=100)
	phone = models.CharField(max_length=10)
	date = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def __str__(self):
		return str(self.customer)+' '+str(self.phone)+' '+str(self.produit)+' '+str(self.qte)


	def placeOrder(self):
		return self.save()

	@staticmethod
	def get_orders_by_customer():
		return Order.objects.all()




