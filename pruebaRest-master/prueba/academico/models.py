from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion =  models.TextField()

    def __str__(self):
        return "{}".format(self.nombre)

    def __unicode__(self):
        return unicode(str(self))

class Alumno(models.Model):
    nombre = models.CharField(max_length=50, help_text='Escribe el nombre del estudiante')
    apellido = models.CharField(help_text='Escribe el apellido del estudiante',max_length=50)
    cedula = models.CharField(max_length=10)
    def __str__(self):
        return "{}".format(self.nombre + self.apellido)

    def __unicode__(self):
        return unicode(str(self))

class Nota(models.Model):
    nota = models.PositiveIntegerField()
    tipo = (('3', 'TERCER TRIMESTRE'),('2','SEGUNDO TRIMESTRE'),('1','PRIMER TRIMESTRE'))
    tipoSolicitud = models.CharField(max_length=1,choices=tipo)
    alumno = models.ForeignKey(Alumno)
    materia = models.ForeignKey('Materia',on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nota)

    def __unicode__(self):
        return unicode(str(self))
