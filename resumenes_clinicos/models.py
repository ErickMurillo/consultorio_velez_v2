from django.db import models

# Create your models here.
SEXO_CHOICES = (('Femenino','Femenino'),('Masculino','Masculino'))

class Paciente(models.Model):
    nombre = models.CharField(max_length = 250)
    edad = models.IntegerField()
    sexo = models.CharField(max_length = 10, choices = SEXO_CHOICES)
    telefono = models.CharField(max_length = 250)
    direccion = models.CharField(max_length = 250)
    app = models.TextField(verbose_name = 'Antecedentes personales patológicos')
    apf = models.TextField(verbose_name = 'Antecedentes familiares')
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name = 'Fecha de ingreso al sistema')


    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete = models.DO_NOTHING)
    fecha_consulta = models.DateField()
    motivo_consulta = models.TextField()
    hea = models.TextField(verbose_name = 'Historial de enfermedades actuales')
    exfx = models.TextField(verbose_name = 'Examen físico')
    dx = models.TextField(verbose_name = 'Diagnóstico')
    tx = models.TextField(verbose_name = 'Tratamiento')
    fecha_prox_consulta = models.DateField()

    def __str__(self):
        return self.paciente.nombre

