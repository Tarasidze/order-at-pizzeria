from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Customer(AbstractUser):

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"

    # def get_absolute_url(self):
    #     return reverse("order:customer-detail", kwargs={"pk": self.pk})


class Ingredients(models.Model):
    ingredient = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.ingredient


class Pizza(models.Model):
    name = models.CharField(max_length=255, unique=True)
    size = models.IntegerField()
    prise = models.IntegerField()
    quantity = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredients, related_name="pizzas")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Name: {self.name}, size: {self.size}, prise: {self.prise}"


class Order(models.Model):
    number_of_order = models.IntegerField(unique=True)
    order_creation_date = models.DateTimeField(auto_now_add=True)
    pizzas = models.ManyToManyField(Pizza, related_name="orders")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")

    class Meta:
        ordering = ["-order_creation_date"]

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["number_of_order", "customer"],
                name="unique order",
            )
        ]
