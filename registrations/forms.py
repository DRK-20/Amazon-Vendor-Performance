from django import forms
from .models import RegisteredProduct
import re

class RegisterProductForm(forms.ModelForm):
    class Meta:
        model = RegisteredProduct
        fields = ['asin']
        widgets = {
            'asin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ASIN',
                'required': 'required',
            })
        }

    def clean_asin(self):
        asin = self.cleaned_data.get('asin').strip().upper()
        
        if not re.match(r'^[A-Z0-9]{10}$', asin):
            raise forms.ValidationError('Enter a valid 10-character ASIN.')

        if RegisteredProduct.objects.filter(asin=asin).exists():
            raise forms.ValidationError('This product is already registered by another user.')

        return asin
