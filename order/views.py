from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render
from django.views import generic

from order.models import Pizza, Customer, Order


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

    return render(request, "order/index.html", context=context)


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
