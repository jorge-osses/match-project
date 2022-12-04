# from django.shortcuts import render, redirect, get_list_or_404
# from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm  # Importamos el Formulario Creado

# Create your views here.


def contact(request):
    contact_form = ContactForm()  # Inicializar el Formulario

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_f = contact_form.save(commit=False)
            contact_f.user = request.user
            contact_f.save()

            return redirect(reverse('contact')+'?ok')
        else:
            return redirect(reverse('contact')+'?error')

    # Agregamos diccionario de contexto
    return render(request, 'register/contact.html', {'form': contact_form})


# # Create your views here.
# class RegisterView(TemplateView):
#     template_name = "register/register.html"
