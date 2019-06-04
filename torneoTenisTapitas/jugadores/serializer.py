from rest_framework import serializers
from .models import jugadores


class JugadoresSerial(serializers.ModelSerializer):
    class Meta:
        model = jugadores
        fields = '__all__'