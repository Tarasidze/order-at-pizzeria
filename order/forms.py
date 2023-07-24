from django import forms
from django.contrib.auth.forms import UserCreationForm

from order.models import Pizza, Ingredients, Customer, Order


class CustomerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by username"})
    )


class CustomerForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
        )


class PizzaSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by name"})
    )


class PizzaForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Pizza
        fields = "__all__"


class OrderForm(forms.ModelForm):
    pizzas = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=Pizza.objects.all(),
    )

    class Meta:
        model = Order
        fields = ['pizzas']  # Exclude 'customer' and 'order_number' fields


class IngredientsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by name"})
    )


class IngredientsSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by name"})
    )


class OrderSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by customer"})
    )
