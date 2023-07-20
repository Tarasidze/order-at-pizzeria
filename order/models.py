from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Customer(AbstractUser):
    date_of_birth = models.DateField()

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"

    # def get_absolute_url(self):
    #     return reverse("order:customer-detail", kwargs={"pk": self.pk})


class Pizza(models.Model):
    name = models.CharField(max_length=255, unique=True)
    size = models.IntegerField()
    prise = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Name: {self.name}, size: {self.size}, prise: {self.prise}"


class Order(models.Model):
    number_of_order = models.IntegerField(unique=True)
    order_creation_date = models.DateTimeField(auto_now_add=True)
    pizzas = models.ManyToManyField(Pizza, related_name="order")
    customer = models.ManyToManyField(Customer, related_name="order")

    class Meta:
        ordering = ["-order_creation_date"]
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "number_of_order"],
                name="unique order"
            )
        ]
