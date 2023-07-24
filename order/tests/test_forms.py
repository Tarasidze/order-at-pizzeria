from django.test import TestCase

from order.forms import OrderForm


class FormsTests(TestCase):
    def test_order_form(self):
        pizza_roma = {
            "name": "Roma",
            "size": 1,
            "price": 190
        }

        form = OrderForm(data=pizza_roma)

        self.assertFalse(form.is_valid())
