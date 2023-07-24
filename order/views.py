from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import FormView
from order.models import Pizza, Customer, Order, Ingredients

from order.forms import (
    PizzaSearchForm,
    PizzaForm,
    IngredientsSearchForm,
    CustomerSearchForm,
    CustomerForm,
    OrderForm,
    OrderSearchForm
)


@login_required
def index(request):
    """View function for the home page of the site."""

    num_pizzas = Pizza.objects.count()
    num_clients = Customer.objects.count()
    num_orders = Order.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_pizzas": num_pizzas,
        "num_clients": num_clients,
        "num_orders": num_orders,
        "num_visits": num_visits + 1,
    }
    print(request.GET.get(1))

    return render(request, "order/index.html", context=context)


class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    pagination = 10
    context_object_name = "customer_list"
    template_name = "order/customer_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = CustomerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Customer.objects.all()

        form = CustomerSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("order:customer-list")


class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("order:customer-list")


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    queryset = Customer.objects.all()
    # user = get_user_object()
    # print("____++++++", queryset)
    # print("____++++++", Customer.objects.all())


class CustomerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Customer
    success_url = reverse_lazy("order:customer-list")


class PizzasListView(LoginRequiredMixin, generic.ListView):
    model = Pizza
    context_object_name = "pizza_list"
    template_name = "order/pizza_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PizzasListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = PizzaSearchForm(initial={"name": name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Pizza.objects.all()

        form = PizzaSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class PizzaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Pizza
    form_class = PizzaForm
    success_url = reverse_lazy("order:pizza-list")


class PizzasDetailView(LoginRequiredMixin, generic.DetailView):
    model = Pizza
    success_url = reverse_lazy("order:pizza-list")


class PizzaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Pizza
    form_class = PizzaForm
    success_url = reverse_lazy("order:pizza-list")


class PizzasDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Pizza
    success_url = reverse_lazy("order:pizza-list")


class IngredientsListView(LoginRequiredMixin, generic.ListView):
    model = Ingredients
    context_object_name = "ingredients_list"
    template_name = "order/ingredients_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(IngredientsListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = IngredientsSearchForm(initial={"name": name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Ingredients.objects.all()

        form = IngredientsSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(ingredient__icontains=form.cleaned_data["name"])

        return queryset


class IngredientsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredients
    fields = "__all__"
    success_url = reverse_lazy("order:ingredients-list")


class IngredientsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredients
    success_url = reverse_lazy("order:ingredients-list")


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    context_object_name = "order_list"
    template_name = "order/order_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(OrderListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = OrderSearchForm(initial={"name": name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Order.objects.all()

        form = OrderSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(customer__username__icontains=form.cleaned_data["name"])

        return queryset


class OrderCreateView(LoginRequiredMixin, FormView):
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy("order:order-list")

    def form_valid(self, form):
        order = form.save(commit=False)
        order.customer = self.request.user
        order.save()

        pizzas = form.cleaned_data['pizzas']
        order.pizzas.set(pizzas)
        order.save()

        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order:order-list")


class UpdateOrderStatusView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        order.completed_order = True
        order.save()
        return redirect('order:order-list')


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("order:order-list")
