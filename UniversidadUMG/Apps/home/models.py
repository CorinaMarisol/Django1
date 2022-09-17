from django.db import models

# Create your models here.
class Estudiante (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' %(self.nombre,self.apellido)


class Publicaciones (models.Model):
    Titulo = models.CharField(max_length=100)
    Noticia = models.CharField(max_length=100)
    Informacion = models.CharField(max_length=300)
    creacion = models.DateTimeField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s %s %s' %(self.Titulo,self.Noticia,self.Informacion)


class Comentarios (models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.CharField(max_length=300)
    publicacion = models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
         return '%s %s %s' %(self.comentario,self.comentario,self.publicacion)