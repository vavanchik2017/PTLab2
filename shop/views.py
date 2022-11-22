from dataclasses import fields

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'amount_order', 'person', 'address']
    def update_price(self):
        getprod = Product.objects.get(id=self.object.product.id)
        if getprod.amount <= getprod.ordered_amount and getprod.flag == 0:
            Product.objects.filter(id=self.object.product.id).update(price=self.object.product.price*1.12,flag=1)
    def form_valid(self, form):
        self.object = form.save()
        prods = Product.objects.get(id=self.object.product.id)
        if (prods.amount - int(self.object.amount_order)) < 0:
            return HttpResponse(f'Ошибка: отсутствует нужное количество!')
        else:
            Product.objects.filter(id=self.object.product.id).update(ordered_amount=prods.ordered_amount + \
                    self.object.amount_order)
            Product.objects.filter(id=self.object.product.id).update(amount=prods.amount - self.object.amount_order)
            PurchaseCreate.update_price(self)
            return HttpResponse(f'Спасибо за покупку! <a href="/">Главная</a>')



