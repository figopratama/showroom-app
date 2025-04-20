from django import forms 
from .models import Car, Service

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('plate_number', 'brand', 'model', 'year', 'price', 'loan', 'interest')
        widgets = {
            'plate_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'brand': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'model': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'year': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'loan': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'interest': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
class NewServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('car', 'date', 'description', 'cost')
        widgets = {
            'car': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'cost': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }