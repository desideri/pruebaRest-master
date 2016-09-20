from rest_framework import serializers
from academico.models import Materia,Alumno,Nota

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ('nombre', 'descripcion',)

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'cedula',)

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ('nota', 'tipo', 'alumno', 'materia',)
