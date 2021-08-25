# Generated by Django 3.2.6 on 2021-08-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_contacto_servicios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='horario_1',
            field=models.CharField(help_text='Ej. Lunes – Viernes: 07:00am – 10:00pm', max_length=250),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='horario_2',
            field=models.CharField(blank=True, help_text='Ej. Lunes – Viernes: 07:00am – 10:00pm', max_length=250, null=True),
        ),
    ]
