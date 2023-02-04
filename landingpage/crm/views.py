from django.shortcuts import render
from .models import Order
from .forms import OrderForm


# Create your views here.

def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm
    return render(request, './index.html', {
        'object_list': object_list,
        'form': form
    })


def thanks_page(request):
    # Передаем данные на страницу
    name = request.POST['name'] # Это поле из передаваемой формы <input name="name">
    phone = request.POST['phone'] # Это поле из передаваемой формы <input name="phone">
    # Записываем данные в БД
    element = Order(order_name = name, order_phone = phone)
    element.save()
    return render(request, './thanks_page.html', {
        'name': name,
        'phone': phone
    })
