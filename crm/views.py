from django.shortcuts import render
from .models import Orders
from .forms import OrderForms


def first_page(request):
    object_list = Orders.objects.all()
    form = OrderForms()
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Orders(order_name = name, order_phone = phone)
    element.save()
    return render(request, './thanks_page.html', {'name': name,
                                                  'phone': phone})