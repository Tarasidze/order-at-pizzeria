from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from order.models import Customer, Pizza, Ingredients

CUSTOMER_URL = reverse("order:customer-list")
PIZZA_URL = reverse("order:pizza-list")
INGREDIENT_LIST = reverse("order:ingredients-list")


class PublicCustomerTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        result = self.client.get(CUSTOMER_URL)

        self.assertNotEquals(result.status_code, 200)


class PrivateCustomerTest(TestCase):
    def setUp(self) -> None:
        self.ethan_hunt = get_user_model().objects.create_user(
           "Username",
           "password123"
        )
        self.doctor_house = get_user_model().objects.create_user(
            "Doctor_House",
            "Two_straight_leg"
        )
        self.client.force_login(self.ethan_hunt)
        self.client.force_login(self.doctor_house)

    def test_retrieve_customer_list(self):
        result = self.client.get(CUSTOMER_URL)
        customers = Customer.objects.all()

        self.assertEquals(result.status_code, 200)
        self.assertEquals(
            list(result.context["customer_list"]),
            list(customers)
        )
        self.assertTemplateUsed(result, "order/customer_list.html")

    def test_customer_search_view(self):
        customers = get_user_model().objects.all()
        result_one = self.client.get(
            f"{CUSTOMER_URL}?username=Doctor_House"
        )
        self.assertIn(
            self.doctor_house,
            list(result_one.context["customer_list"])
        )
        self.assertNotIn(
            self.ethan_hunt,
            list(result_one.context["customer_list"])
        )
        result_two = self.client.get(
            f"{CUSTOMER_URL}?username="
        )
        self.assertEquals(
            list(customers),
            list(result_two.context["customer_list"])
        )


class PizzaCustomerTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        result = self.client.get(PIZZA_URL)

        self.assertNotEquals(result.status_code, 200)


class PrivatePizzaTest(TestCase):
    def setUp(self) -> None:
        self.ethan_hunt = get_user_model().objects.create_user(
           "Username",
           "password123"
        )
        self.client.force_login(self.ethan_hunt)
        self.pizza_roma = Pizza.objects.create(
            name="Roma",
            size=1,
            price=190
        )
        self.pizza_winter = Pizza.objects.create(
            name="Winter",
            size=3,
            price=399
        )
        super().setUp()

    def test_retrieve_pizza_list(self):
        result = self.client.get(PIZZA_URL)
        pizzas = Pizza.objects.all()

        self.assertEquals(result.status_code, 200)
        self.assertEquals(
            list(result.context["pizza_list"]),
            list(pizzas)
        )
        self.assertTemplateUsed(result, "order/pizza_list.html")

    def test_customer_search_view(self):
        pizzas = Pizza.objects.all()
        result_one = self.client.get(
            f"{PIZZA_URL}?name=roma"
        )
        self.assertIn(
            self.pizza_roma,
            list(result_one.context["pizza_list"])
        )
        self.assertNotIn(
            self.pizza_winter,
            list(result_one.context["pizza_list"])
        )
        result_two = self.client.get(
            f"{PIZZA_URL}?username="
        )
        self.assertEquals(
            list(pizzas),
            list(result_two.context["pizza_list"])
        )


class PrivateIngredientsTest(TestCase):
    def setUp(self) -> None:
        self.ethan_hunt = get_user_model().objects.create_user(
           "Username",
           "password123"
        )
        self.client.force_login(self.ethan_hunt)
        self.salo = Ingredients.objects.create(
            ingredient="salo"
        )
        self.tomato = Ingredients.objects.create(
            ingredient="tomato"
        )
        # super().setUp()

    def test_retrieve_pizza_list(self):
        result = self.client.get(INGREDIENT_LIST)
        ingredients = Ingredients.objects.all()

        self.assertEquals(result.status_code, 200)
        self.assertEquals(
            list(result.context["ingredients_list"]),
            list(ingredients)
        )
        self.assertTemplateUsed(result, "order/ingredients_list.html")

    def test_customer_search_view(self):
        pizzas = Pizza.objects.all()
        result_one = self.client.get(
            f"{PIZZA_URL}?name=roma"
        )
        self.assertIn(
            self.pizza_roma,
            list(result_one.context["pizza_list"])
        )
        self.assertNotIn(
            self.pizza_winter,
            list(result_one.context["pizza_list"])
        )
        result_two = self.client.get(
            f"{PIZZA_URL}?username="
        )
        self.assertEquals(
            list(pizzas),
            list(result_two.context["pizza_list"])
        )




