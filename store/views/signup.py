from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.costumer import Customer

print(make_password('1234'))


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('Password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,

        }
        error_message = None

        costumer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            phone=phone,
                            password=password)

        error_message = self.validateCustomer(costumer)

        # saving_values

        if not error_message:
            print(first_name, last_name, phone, email, password)
            costumer.password = make_password(costumer.password)
            costumer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, costumer):

        error_message = None;
        if not costumer.first_name:
            error_message = 'First Name is Required!!'
        elif len(costumer.first_name) < 4:
            error_message = 'First Name should not be less than 4 characters!!'

        elif not costumer.last_name:
            error_message = 'Last Name is Required!!'
        elif len(costumer.last_name) < 4:
            error_message = 'Last Name should not be less than 4 characters!!'

        elif not costumer.email:
            error_message = 'Email is Required!!'
        elif len(costumer.email) < 4:
            error_message = 'E-mail should not be less than 4 characters!!'

        elif not costumer.password:
            error_message = 'Password is Required!!'
        elif len(costumer.password) < 6:
            error_message = 'Password should not be less than 8 characters!!'

        elif not costumer.phone:
            error_message = 'Phone Number is Required!!'
        elif len(costumer.phone) < 10:
            error_message = 'Phone Number should not be less than 10 characters!!'


        elif costumer.isExists():
            error_message = 'Email already Registered..'

        return error_message
