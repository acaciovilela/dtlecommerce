from django import forms
from .models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        def clean_price(self):
            if self.cleaned_data['price'] <= 0:
                raise forms.ValidationError('Preço deve ser maior que zero.')
                return self.cleaned_data['price']

class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'size':'2',
                'value':'1',
                'maxlength':'5',
                'class': 'form-control'
            }
        ),
        error_messages={'invalid':'Please enter a valid quantity.'},
        min_value=1
    )
    product_slug = forms.CharField(widget=forms.HiddenInput())
