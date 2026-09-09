from django import forms

from .models import Product, Supplier


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            "name",
            "email",
            "phone",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Supplier name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "supplier@example.com",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Phone number",
                }
            ),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "sku",
            "cost_price",
            "selling_price",
            "low_stock_threshold",
            "description",
            "supplier",
            "is_active",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Product name",
                }
            ),
            "sku": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "SKU",
                }
            ),
            "cost_price": forms.NumberInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "selling_price": forms.NumberInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "low_stock_threshold": forms.NumberInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "min": "0",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "rows": 4,
                    "placeholder": "Product description",
                }
            ),
            "supplier": forms.Select(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-lg "
                             "focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "h-4 w-4 text-blue-600 rounded",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        cost_price = cleaned_data.get("cost_price")
        selling_price = cleaned_data.get("selling_price")

        if (
            cost_price is not None
            and selling_price is not None
            and selling_price < cost_price
        ):
            raise forms.ValidationError(
                "Selling price cannot be lower than cost price."
            )

        return cleaned_data
