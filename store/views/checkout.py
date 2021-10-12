from django.shortcuts import render, redirect
from store.models.costumer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.orders import Orders


class CheckOut(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        costumer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, costumer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Orders(customer = Customer(id = costumer),
                       product = product,
                       price = product.price,
                       address = address,
                       phone = phone,
                       quantity = cart.get(str(product.id)))
            order.save()
            request.session['cart'] = {}

        return redirect('cart')
