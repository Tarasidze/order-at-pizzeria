from django.urls import path

from .views import (
    index,
    PizzasListView,
    PizzasDetailView,
    PizzaCreateView,
    PizzasDeleteView,
    IngredientsListView,
    IngredientsCreateView,
    IngredientsDeleteView,
    CustomerListView,
    CustomerCreateView,
    CustomerDetailView,
    CustomerDeleteView,
    CustomerUpdateView,
    OrderListView,
    OrderCreateView,
    OrderUpdateView,
    PizzaUpdateView,
    OrderDeleteView,
    UpdateOrderStatusView,

)

urlpatterns = [
    path("", index, name="index"),
    path("pizzas/", PizzasListView.as_view(), name="pizza-list"),
    path("pizzas/create/", PizzaCreateView.as_view(), name="pizza-create"),
    path("pizza/<int:pk>/update/", PizzaUpdateView.as_view(), name="pizza-update"),
    path("pizzas/<int:pk>/delete/", PizzasDeleteView.as_view(), name="pizza-delete"),
    path("pizzas/<int:pk>/detail/", PizzasDetailView.as_view(), name="pizza-detail"),

    path("ingredients/", IngredientsListView.as_view(), name="ingredients-list"),
    path("ingredients/create/", IngredientsCreateView.as_view(), name="ingredients-create"),
    path("ingredients/<int:pk>/delete/", IngredientsDeleteView.as_view(), name="ingredients-delete"),

    path("customer/", CustomerListView.as_view(), name="customer-list"),
    path("customer/create", CustomerCreateView.as_view(), name="customer-create"),
    path("customer/<int:pk>/update/", CustomerUpdateView.as_view(), name="customer-update"),
    path("customer/<int:pk>/delete/", CustomerDeleteView.as_view(), name="customer-delete"),
    path("customer/<int:pk>/detail/", CustomerDetailView.as_view(), name="customer-detail"),

    path("order/", OrderListView.as_view(), name="order-list"),
    path("order/create/", OrderCreateView.as_view(), name="order-create"),
    path("order/<int:pk>/update/", OrderUpdateView.as_view(), name="order-update"),
    path('order/<int:pk>/update-status/', UpdateOrderStatusView.as_view(), name='update_order_status'),
    path("order/<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),

]

app_name = "order"
