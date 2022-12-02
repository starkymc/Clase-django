from operator import mod
from tkinter import CASCADE
from django.db import models



# Clase Persona Abstract
class Persona(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    #Funcion
    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        abstract = True


#Creacion de tabla Alumno
#Heredando de clase Persona
class Profesor(Persona):
    salario = models.FloatField(default=99)
    #Poniendo primary key multiple y cambiando nombre del primary key
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id', 'first_name', 'last_name'], name = 'primary_key_profesor' 
            )
        ]   


#Creacion de tabla Salon REFERENCIA (PROFESOR)
class Salon(models.Model):
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()
    #idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, default=0)
    idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

#Creacion de tabla Alumno REFERENCIA (SALON)
#Heredando de clase Persona
class Alumno(Persona):
    # Enlanzando Tabla Salon en CASCADE
    idSalon = models.ForeignKey(Salon, on_delete=models.CASCADE)


    #Poniendo primary key multiple
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id', 'first_name', 'last_name'], name = 'primary_key_alumno' 
            )
        ]   


# Proxy de Modelo Alumno
class OrdenarAlumno(Alumno):
    class Meta:
        ordering = ['last_name']
        proxy = True

# Proxy de Modelo Salon
class OrdenarSalon(Salon):
    class Meta:
        ordering = ['hora_entrada']
        proxy = True


# Clase Persona Abstract
class Evaluacion(models.Model):
    hora_fecha = models.DateTimeField()
    curso = models.CharField(max_length=30)
    evaluador = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Examen_Final(Evaluacion):
    Duracion = models.IntegerField()
    n_preguntas = models.IntegerField()
    puntaje_total = models.IntegerField()

    def puntaje_preguntas(self):
        return self.puntaje_total / self.n_preguntas

class Proyecto(Evaluacion):
    tema_proyecto = models.CharField(max_length=100)
    n_grupos = models.IntegerField()

#Proxy 
class OrderedNameProyect(Proyecto):  
    class Meta:
        proxy= True
        ordering = ['tema_proyecto']


