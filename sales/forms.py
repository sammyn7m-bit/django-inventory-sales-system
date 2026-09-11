from django import forms

from .models import Customer

# get customer details 
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "name",
            "phone",
            "email",
            "address",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full rounded-lg border-gray-300 "
                         "focus:border-blue-500 focus:ring-blue-500",
                "placeholder": "Your name",
            }),

            "phone": forms.TextInput(attrs={
                "class": "w-full rounded-lg border-gray-300 "
                         "focus:border-blue-500 focus:ring-blue-500",
                "placeholder": "Phone number",
            }),

            "email": forms.EmailInput(attrs={
                "class": "w-full rounded-lg border-gray-300 "
                         "focus:border-blue-500 focus:ring-blue-500",
                "placeholder": "Email address",
            }),

            "address": forms.TextInput(attrs={
                "class": "w-full rounded-lg border-gray-300 "
                         "focus:border-blue-500 focus:ring-blue-500",
                "placeholder": "Delivery address",
            }),
        }
