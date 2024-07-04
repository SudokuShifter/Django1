import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order, FAKE
# Create your views here.


def main(request):
    return render(request, 'secondapp/main.html')


def fill_users_data(request):
    for i in range(9):
        Client.add_new_user()
    return HttpResponse('Fill data was end')


def check_users(request):
    return HttpResponse(Client.get_all_users())


def add_new_user(request):
    return HttpResponse(Client.add_new_user())


def update_user_name(request, some_id):
    return HttpResponse(Client.update_user_name(some_id))


def delete_user(request, some_id):
    return HttpResponse(Client.user_delete(some_id))


def fill_product_data(request):
    for i in range(9):
        Product.add_new_product()
    return HttpResponse('Fill data was end')


def check_products(request):
    return HttpResponse(Product.get_all_products())


def update_product_name(request, some_id):
    return HttpResponse(Product.update_name_product(some_id))


def delete_product(request, some_id):
    return HttpResponse(Product.delete_product(some_id))


def fill_order_data(request):
    for i in range(9):
        Order.add_order()
    return HttpResponse('Fill data was end')


def check_orders(request):
    return HttpResponse(Order.get_orders())


def update_order_products(request, some_id):
    return HttpResponse(Order.update_order(some_id))


def delete_order(request, some_id):
    return HttpResponse(Order.delete_order(some_id))


def check_statistic(request, count):
    list_orders = Order.get_orders_in_range_date(count)
    for order in list_orders:
        order.unique_products = order.product.distinct()
    context = {
        'title': 'Data',
        'names': list_orders,
    }
    return render(request, 'secondapp/orders_data.html', context)


