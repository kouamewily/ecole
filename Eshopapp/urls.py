
from django.urls import path
from .views.home import Index
from .views.login import Login, logout
from .views.signup import SignUp
from .views.cart import Cart
from .views.checkout import Checkout
from .views.order import OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
   
    path('acceuil/', Index.as_view(), name='index'),
    path('Creer-compte', SignUp.as_view(), name='signup'),
    path('', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('panier/', Cart.as_view(), name='panier'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('cmd/', auth_middleware(OrderView.as_view()), name='cmd'),
    
]