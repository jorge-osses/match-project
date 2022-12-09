# Generated by Django 4.0.6 on 2022-12-09 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_contact_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='childs',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Cantidad Hijos'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='drink',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Bebida'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='food',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Comida'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='music',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Música'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nacionality',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='profession',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Profesión'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sport',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Deporte Preferido'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado Civil'),
        ),
    ]
