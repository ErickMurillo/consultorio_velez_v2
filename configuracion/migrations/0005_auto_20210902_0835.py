# Generated by Django 3.2.6 on 2021-09-02 14:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0004_contacto_telefono_consultorio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='servicios',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
