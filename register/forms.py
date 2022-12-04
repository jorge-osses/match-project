from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'lastname', 'gender', 'nacionality', 'profession', 'status', 'childs',
                  'sport', 'music', 'food', 'drink', 'contact_type', 'subscription']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Género'}),
            'nacionality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidad'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profesión'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado civil'}),
            'childs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad Hijos'}),
            'sport': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Deporte que le gusta'}),
            'music': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Música que le gusta'}),
            'food': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comida favorita'}),
            'drink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bebida favorita'}),
        }
        labels = {
            'name': '', 'lastname': '', 'gender': '', 'nacionality': '', 'profession': '', 'status': '', 'childs': '', 'sport': '', 'music': '', 'food': '', 'drink': ''
        }
