from academico.models import *
from academico.serializers import MateriaSerializer, AlumnoSerializer, NotaSerializer
from rest_framework import viewsets

class MateriaViewSet(viewsets.ModelViewSet):

    serializer_class = MateriaSerializer
    queryset = Materia.objects.all()

class AlumnoViewSet(viewsets.ModelViewSet):

    serializer_class = AlumnoSerializer
    queryset = Alumno.objects.all()

class NotaViewSet(viewsets.ModelViewSet):

    serializer_class = NotaSerializer
    queryset = Nota.objects.all()
