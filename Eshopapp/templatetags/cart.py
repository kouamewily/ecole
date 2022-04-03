from django import template


register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(prod, cart):

	keys = cart.keys()

	for id in keys:

		if int(id) == prod.id:
			return True

	return False;


@register.filter(name='cart_quantity')
def cart_quantity(prod, cart):

	keys = cart.keys()

	for id in keys:

		if int(id) == prod.id:
			return cart.get(id)

	return 0;

@register.filter(name='price_total')
def price_total(prod, cart):
	return prod.prix * cart_quantity(prod, cart)

@register.filter(name='total_cart_price')
def total_cart_price(prod, cart):
	total = 0;
	for p in prod:
		total+= price_total(p, cart)

	return total