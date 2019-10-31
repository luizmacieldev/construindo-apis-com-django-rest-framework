from rest_framework import serializers
from alunos.models import Aluno

# serializar = transformar em JSON (Javascript object notation)

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('__all__')
