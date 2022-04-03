from django import template


register = template.Library()

@register.filter(name='monaie')
def monaie(numero):	

	return str(numero) + " Fcfa" 


@register.filter(name='multiply')
def multiply(numero, num):	

	return numero * num