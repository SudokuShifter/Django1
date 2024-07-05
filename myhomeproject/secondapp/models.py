from django.db import models
from django.utils import timezone
from faker import Faker
from random import randint, choice, choices
from datetime import date, timedelta

FAKE = Faker('ru_RU')


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    number_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    date_registration = models.DateField(default=timezone.datetime.now())

    @staticmethod
    def get_all_users():
        clients = Client.objects.all()
        if clients:
            return clients
        return 'Clients not found'

    @staticmethod
    def add_new_user():
        client = Client(name=FAKE.first_name(),
                        email=FAKE.email(),
                        number_phone=FAKE.phone_number(),
                        address=FAKE.address(),
                        date_registration=FAKE.date())
        client.save()

    @staticmethod
    def update_user_name(some_id):
        client = Client.objects.get(pk=some_id)
        client.name = FAKE.first_name()
        client.save()
        return client.name

    @staticmethod
    def user_delete(some_id):
        client = Client.objects.get(pk=some_id)
        if client is not None:
            client.delete()
        return f'Client with id {some_id} was deleted'

    def __str__(self):
        return f'{self.name} with {self.email} was registered {self.date_registration}\n'


class Product(models.Model):
    name = models.CharField(max_length=20, default='Пусто')
    description = models.TextField(default='Очень интересный товар')
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    date_add_product = models.DateField(default=timezone.datetime.now())
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    @staticmethod
    def get_all_products():
        products = Product.objects.all()
        if products is not None: return products
        return 'Products not found'

    @staticmethod
    def add_new_product():
        product = Product(name=FAKE.text(max_nb_chars=10),
                          description=FAKE.text(max_nb_chars=30),
                          price=randint(20, 40) / 0.2,
                          quantity=randint(10, 20),
                          image=FAKE.image())
        product.save()
        return product

    @staticmethod
    def update_name_product(some_id):
        product = Product.objects.get(pk=some_id)
        product.name = 'Теперь другой продукт'
        product.save()
        return product

    @staticmethod
    def delete_product(some_id):
        product = Product.objects.get(pk=some_id)
        product.delete()
        return f'Product with id {some_id} was deleted'

    def __str__(self):
        return f'{self.name} - {self.description}. Quantity: {self.quantity}. Price: {self.price}\n'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    sum_of_order = models.FloatField()
    date_order = models.DateField(default=timezone.datetime.now())

    @staticmethod
    def add_order():
        """
        На самом деле не знаю до какого момента это всё можно оптимизировать, но очень долго)
        """
        products = choices(Product.objects.all(), k=5)
        price = sum([i.price for i in products])
        order = Order(client=choice(Client.objects.all()),
                      sum_of_order=price,
                      date_order=FAKE.date_between_dates(date.today() - timedelta(days=365), date.today()))
        order.save()
        order.product.set(products)

        for i in products:
            if i.quantity <= 0:
                i.quantity = 100
                print('Пришла поставка')
            else:
                i.quantity -= 1
            i.save()

    @staticmethod
    def get_orders():
        orders = Order.objects.all()
        return orders

    @staticmethod
    def update_order(some_id):
        order = Order.objects.get(pk=some_id)
        new_products = choices(Product.objects.all(), k=4)
        order.product.set(new_products)
        order.sum_of_order = sum(product.price for product in new_products)
        order.save()
        return order

    @staticmethod
    def delete_order(some_id):
        order = Order.objects.get(pk=some_id)
        order.delete()
        return f'Order with id {some_id} was deleted'

    @staticmethod
    def get_orders_in_diapason(some_date):
        return (Order.objects.order_by('date_order').
                filter(date_order__gte=date.today() - timedelta(days=some_date)))

    @staticmethod
    def get_orders_in_range_date(some_point):
        match some_point:
            case 1:
                return Order.get_orders_in_diapason(7)
            case 2:
                return Order.get_orders_in_diapason(30)
            case 3:
                return Order.get_orders_in_diapason(365)

    def __str__(self):
        return f'{self.client} was create order {self.pk} with {self.product}. Price: {self.sum_of_order}'
