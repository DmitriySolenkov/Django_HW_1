from django import forms
import datetime


class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Название товара'}))
    description = forms.CharField(max_length=100, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Описание товара'}))
    price = forms.DecimalField(decimal_places=2, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Цена товара'}))
    amount = forms.IntegerField(min_value=1, max_value=50, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Количество'}))
    addition_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))
    image = forms.ImageField()
