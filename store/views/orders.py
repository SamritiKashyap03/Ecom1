from django.shortcuts import render, redirect
from store.models.costumer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.orders import Orders
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderView(View):

     def get(self,request):
         customer = request.session.get('customer')
         orders = Orders.get_orders_by_customer(customer).order_by('-date')
         print(orders)

         return render(request , 'orders.html' , {'orders' : orders})

