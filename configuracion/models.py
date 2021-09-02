from django.db import models
from solo.models import SingletonModel
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField

# Create your models here.
class Inicio(SingletonModel):
    nombre = models.CharField(max_length = 250)
    descripcion = models.CharField(max_length = 250)
    telefono = models.CharField(max_length = 250)
    direccion = models.CharField(max_length = 250)
    foto = ImageField(upload_to='fotos', help_text = '490x360')
    titulo_1 = models.CharField(max_length = 250)
    texto_1 = models.TextField()
    titulo_2 = models.CharField(max_length = 250)
    texto_2 = models.TextField()
    titulo_3 = models.CharField(max_length = 250)
    texto_3 = models.TextField()

    def __str__(self):
        return "Inicio"

    class Meta:
        verbose_name = "1. Inicio"

class Informacion(SingletonModel):
    texto_1 = models.CharField(max_length = 250)
    texto_2 = models.CharField(max_length = 250)
    descripcion = models.TextField()
    foto = ImageField(upload_to='fotos', help_text = '400x520')

    def __str__(self):
        return "Información"

    class Meta:
        verbose_name = "2. Información"

class Servicios(models.Model):
    titulo = models.CharField(max_length = 250)
    descripcion = RichTextField()

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "3. Servicios"
        verbose_name_plural = "3. Servicios"
        ordering = ('id',)

class Contacto(SingletonModel):
    texto = models.CharField(max_length = 250)
    # descripcion = models.TextField()
    horario_1 = models.CharField(max_length = 250,help_text="Ej. Lunes – Viernes: 07:00am – 10:00pm")
    horario_2 = models.CharField(max_length = 250, null = True, blank = True,help_text="Ej. Lunes – Viernes: 07:00am – 10:00pm")
    correo = models.EmailField() 
    telefono_consultorio = models.CharField(max_length = 250)

    def __str__(self):
        return "Contacto"

    class Meta:
        verbose_name = "4. Contacto"