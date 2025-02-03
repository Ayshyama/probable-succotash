from django import forms
from .models import Order, OrderItem
from django.utils.timezone import now

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'billing_name', 'billing_address', 'billing_zip_city', 'billing_email', 'billing_phone',
            'same_as_billing', 'shipping_name', 'shipping_address', 'shipping_zip_city',
            'parking_spot', 'signature'
        ]
        widgets = {
            'same_as_billing': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'id_same_as_billing'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date_display'] = forms.CharField(
            initial=now().date(),  # pre-fill today’s date
            required=False,
            widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        )
        self.fields['date_location_display'] = forms.CharField(
            initial=f"{now().date()}, Karlsruhe",
            required=False,
            widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        )


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }
