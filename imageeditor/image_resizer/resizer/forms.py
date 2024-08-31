from django import forms
from .models import ImageResize

class ImageResizerForm(forms.ModelForm):
    class Meta:
        model = ImageResize
        fields = {'image','resize_percentage'}
        widgets = {
            'resize_percentage':forms.NumberInput(attrs={'min': 1 , 'max' :100}),
        }