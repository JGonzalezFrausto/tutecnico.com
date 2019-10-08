from django.db import models

# Create your models here.

class Tecnico(models.Model):
    ApellidoPaterno = models.CharField(max_length=35, null= True)
    ApellidoMaterno = models.CharField(max_length=35, null= True)
    Nombres = models.CharField(max_length=35, null= True)
    Servicio = models.CharField(max_length=300, null= True)
    Telefono = models.CharField(max_length=10, null= True)
    Email = models.EmailField()
    Direccion = models.CharField(max_length=300, null= True)
    CodigoPostal = models.CharField(max_length= 5, null= True)

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format (self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

  
    def __str__ (self):
        return self.NombreCompleto()
        


class Actividades(models.Model):
    Servicioprestado= models.CharField(max_length= 50)
    
    def __str__(self):
        return self.Servicioprestado

class IdTecnico (models.Model):
    Tecnico = models.ForeignKey(Tecnico, null= False, blank= False, on_delete= models.CASCADE)
    Actividades = models.ForeignKey(Actividades, null= False, blank= False, on_delete= models.CASCADE)
    FechaAlta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = " {0} => {1} "
        return cadena.format(self.Tecnico, self.Actividades)


