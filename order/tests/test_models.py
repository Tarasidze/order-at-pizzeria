from django.contrib.auth import get_user_model
from django.test import TestCase

from order.models import Customer, Ingredients, Pizza


class ModelTest(TestCase):
    def test_customer_str(self):
        customer = Customer.objects.create(
            username="admin",
            first_name="Gomer",
            last_name="Simpson",
        )
        self.assertEquals(
            str(customer),
            f"{customer.username} {customer.first_name} {customer.last_name}"
        )

    def test_customer_credential(self):
        username_ = "Futurama"
        first_name_ = "Fry"
        last_name_ = "Philip"
        password_ = "KreksPeks@123"

        customer = get_user_model().objects.create_user(
            username=username_,
            password=password_,
            first_name=first_name_,
            last_name=last_name_,
        )

        self.assertEquals(customer.username, username_)
        self.assertEquals(customer.first_name, first_name_)
        self.assertEquals(customer.last_name, last_name_)
        self.assertTrue(customer.check_password(password_))

    def test_Ingredients_str(self):
        ingredient_ = Ingredients.objects.create(
            ingredient="tomato"
        )
        self.assertEquals(
            str(ingredient_),
            f"{ingredient_.ingredient}"
        )

    def test_pizza_str(self):
        pizza = Pizza.objects.create(
            name="Roma",
            size=1,
            price="190"

        )
        self.assertEquals(
            str(pizza),
            f"Name: {pizza.name}, size: {pizza.size}, prise: {pizza.price}"
        )
