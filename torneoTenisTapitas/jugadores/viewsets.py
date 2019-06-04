from rest_framework import viewsets 
from .models import jugadores
from .serializer import JugadoresSerial

class jugadorViewsets(viewsets.ModelViewSet):
    queryset = jugadores.objects.all()
    serializer_class = JugadoresSerial