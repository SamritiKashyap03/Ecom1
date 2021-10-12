from django.shortcuts import render, redirect , HttpResponseRedirect
from store.models.costumer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password, check_password

print(make_password('1234'))
class Login(View):
    return_url = None

    def get(self, request):
        print('hello')
        Login.return_url = request.GET.get('return_url')
        print(f'a {Login.return_url}')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('Password')
        costumer = Customer.get_costumer_by_email(email)
        error_message = None
        if costumer:
            flag = check_password(password, costumer.password)
            if flag:
                request.session['customer'] = costumer.id

                print('you are : ', request.session.get('email'))

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email OR Password invalid !!'
        else:
            error_message = 'Email OR Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

    def logout(request):
        request.session.clear()
        return redirect('login')

