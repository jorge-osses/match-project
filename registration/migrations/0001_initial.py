# Generated by Django 4.0.6 on 2022-12-14 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to=registration.models.custom_upload_to)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('message', models.TextField(max_length=500, verbose_name='Mensaje')),
                ('gender', models.CharField(blank=True, max_length=50, null=True, verbose_name='Género')),
                ('nacionality', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nacionalidad')),
                ('profession', models.CharField(blank=True, max_length=50, null=True, verbose_name='Profesión')),
                ('status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado Civil')),
                ('childs', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cantidad Hijos')),
                ('sport', models.CharField(blank=True, max_length=50, null=True, verbose_name='Deporte Preferido')),
                ('music', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Música')),
                ('food', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Comida')),
                ('drink', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Bebida')),
                ('contact_type', models.CharField(choices=[('Presencial', 'presencial'), ('On-line', 'on-line')], default='Presencial', max_length=10, verbose_name='Tipo de Contacto')),
                ('subscription', models.BooleanField(default=False, verbose_name='Suscribirme a Correos Informativos')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Envío')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
    ]
