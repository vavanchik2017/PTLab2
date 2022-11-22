from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(blank=True, null=True, default=0)
    ordered_amount = models.PositiveIntegerField(blank=True, null=True, default=0)
    flag = models.BooleanField(default=False)



class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    amount_order = models.PositiveIntegerField(blank=True, null=True, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def get_amount_of_prod(self):
        return
