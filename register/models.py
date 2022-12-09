from django.db import models
from django.contrib.auth.models import User

# Create your models here.


options = [
    [0, 'Presencial'],
    [1, 'On Line']
]


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # link = models.IntegerField(User.id)
    # avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo Electrónico')
    message = models.TextField(verbose_name='Mensaje')
    gender = models.CharField(
        max_length=50, verbose_name='Género', null=True, blank=True)
    nacionality = models.CharField(
        max_length=50, verbose_name='Nacionalidad', null=True, blank=True)
    profession = models.CharField(
        max_length=50, verbose_name='Profesión', null=True, blank=True)
    status = models.CharField(
        max_length=50, verbose_name='Estado Civil', null=True, blank=True)
    childs = models.CharField(
        max_length=50, verbose_name='Cantidad Hijos', null=True, blank=True)
    sport = models.CharField(
        max_length=50, verbose_name='Deporte Preferido', null=True, blank=True)
    music = models.CharField(
        max_length=50, verbose_name='Tipo de Música', null=True, blank=True)
    food = models.CharField(
        max_length=50, verbose_name='Tipo de Comida', null=True, blank=True)
    drink = models.CharField(
        max_length=50, verbose_name='Tipo de Bebida', null=True, blank=True)
    contact_type = models.IntegerField(
        choices=options, verbose_name='Tipo de Contacto')
    subscription = models.BooleanField(
        default=False, verbose_name='Suscribirme a Correos Informativos')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Envío')
