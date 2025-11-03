from django import forms
from .models import Skuter

class SkuterForm(forms.ModelForm):
    class Meta:
        model = Skuter
        fields = ['nom', 'model', 'narx_soat', 'mavjud', 'rasm', 'tavsif']
        widgets = {
            'tavsif': forms.Textarea(attrs={'rows':4}),
        }
