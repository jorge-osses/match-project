from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.pic.delete()
    return 'pictures/' + filename

options = [
    ('Presencial', 'presencial'),
    ('On-line', 'on-line'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
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
    contact_type = models.CharField(
        max_length=10,
        choices=options,
        default='Presencial',
        verbose_name='Tipo de Contacto')
    subscription = models.BooleanField(
        default=False, verbose_name='Suscribirme a Correos Informativos')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Envío')

    class Meta:
        ordering =['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")