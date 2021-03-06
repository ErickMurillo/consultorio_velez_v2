# Generated by Django 3.2.6 on 2021-08-20 16:51

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_1', models.CharField(max_length=250)),
                ('texto_2', models.CharField(max_length=250)),
                ('descripcion', models.TextField()),
                ('foto', sorl.thumbnail.fields.ImageField(help_text='400x520', upload_to='fotos')),
            ],
            options={
                'verbose_name': '2. Información',
            },
        ),
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('foto', sorl.thumbnail.fields.ImageField(help_text='490x360', upload_to='fotos')),
                ('titulo_1', models.CharField(max_length=250)),
                ('texto_1', models.TextField()),
                ('titulo_2', models.CharField(max_length=250)),
                ('texto_2', models.TextField()),
                ('titulo_3', models.CharField(max_length=250)),
                ('texto_3', models.TextField()),
            ],
            options={
                'verbose_name': '1. Inicio',
            },
        ),
    ]
