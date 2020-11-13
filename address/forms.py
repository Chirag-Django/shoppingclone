from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ('billing_details',)

# class BillingAddressForm(forms.ModelForm):
#     class Meta:
#         model = BillingAddress
#         fields = '__all__'

