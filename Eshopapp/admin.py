from django.contrib import admin
from .models import Produit, Categorie, Customer, Order


class ProduitAdmin(admin.ModelAdmin):
	list_display = ['nom', 'prix', 'cat']



class CategorieAdmin(admin.ModelAdmin):
	list_display = ['nom']

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Customer)
admin.site.register(Order)
