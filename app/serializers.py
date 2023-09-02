from rest_framework import serializers
from .models import *

class MarcasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = ["id", "nome", "localizacao"]

class CarrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carros
        fields = ["id", "nome", "preco", "marca_id", "ano"]
        
