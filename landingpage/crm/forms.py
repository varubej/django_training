from django import forms


class OrderForm(forms.Form):
    # Указав доп параметр widget можно передавать доп параметры такие как стиль. Танный пример подтягивает стиль который находится на страницу исполнения
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
        'class': 'css_input'
    }))
    phone = forms.CharField(max_length=200)
