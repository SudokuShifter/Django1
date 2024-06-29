from django.urls import path
from . import views

urlpatterns = [
    path('fill_users/', views.fill_users_data, name='fill_data_user'),
    path('get_users/', views.check_users, name='get_users'),
    path('update_user/<some_id>/', views.update_user_name, name='update_user_name'),
    path('delete_user/<some_id>/', views.delete_user, name='delete_user'),
    path('add_user/', views.add_new_user, name='add_user'),
    path('fill_products/', views.fill_product_data, name='fill_data_product'),
    path('get_products/', views.check_products, name='get_products'),
    path('update_product/<some_id>', views.update_product_name, name='update_product_name'),
    path('delete_product/<some_id>', views.delete_product, name='delete_product'),
    path('fill_orders/', views.fill_order_data, name='fill_order_data'),
    path('get_orders/', views.check_orders, name='get_orders'),
    path('update_order/<some_id>', views.update_order_products, name='update_order_products'),
    path('delete_order/<some_id>', views.delete_order, name='delete_order'),
]