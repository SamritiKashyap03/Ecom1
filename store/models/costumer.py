from django.db import models



class Customer(models.Model):
    first_name = models.CharField(max_length = 50, default=" ")
    last_name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20 )

    def register(self):
        self.save()

    @staticmethod
    def get_costumer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False