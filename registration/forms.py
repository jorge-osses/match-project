from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, intente con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pic', 'name', 'lastname', 'gender', 'nacionality', 'profession', 'status', 'childs',
                  'sport', 'music', 'food', 'drink', 'contact_type', 'subscription']
        widgets = {
            'pic': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'name': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nombre'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Apellido'}),
            'gender': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Género'}),
            'nacionality': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nacionalidad'}),
            'profession': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Profesión'}),
            'status': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Estado civil'}),
            'childs': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Cantidad Hijos'}),
            'sport': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Deporte que le gusta'}),
            'music': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Música que le gusta'}),
            'food': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Comida favorita'}),
            'drink': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Bebida favorita'}),
            'contact_type': forms.Select(attrs={'class': 'form-control mt-3', 'placeholder': 'Encuentro'}),
        }
        labels = {
            'name': '',
            'lastname': '',
            'gender': '',
            'nacionality': '',
            'profession': '',
            'status': '',
            'childs': '',
            'sport': '',
            'music': '',
            'food': '',
            'drink': '',
            'Pic': '',
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
    
    class Meta:
        model = User
        fields = ['email']
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, intente con otro.")
        return email