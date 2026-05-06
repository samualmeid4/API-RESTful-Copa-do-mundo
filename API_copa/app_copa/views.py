from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Grupo, Tecnico, Selecao, Jogador, Jogo, EventoJogo
from .serializers import GrupoSerializer, JogadorSerializer, TecnicoSerializer, SelecaoSerializer, Jogador, JogoSerializer, EventoJogoSerializer

# Create your views here.


# class GrupoProxy(viewsets.ViewSet):
#     def get(self, request, pk=None):
#         url = f"http://localhost:8000/api/grupos/"
#         if pk is not None:
#             url = f"{url}{pk}/"

#         res = requests.get(url)
#         data = add_hateoas(res.json(), "products")
#         return Response(data)
    


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    filter_backends =[SearchFilter]
    search_fields = ['nome']

class SelecaoViewSet(viewsets.ModelViewSet):
    queryset = Selecao.objects.all()
    serializer_class = SelecaoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['grupo']
    search_fields = ['nome', 'sigla']

class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.select_related('selecao').all()
    serializer_class = JogadorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['selecao', 'posicao', 'suspenso']
    search_fields = ['nome', 'nome_guerra']
    ordering_fields = ['selecao', 'numero_camisa']

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.select_related('selecao_mandante', 'selecao_visitante', 'grupo').prefetch_related('eventos','eventos__jogador').all()
    serializer_class = JogoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['fase', 'status', 'grupo']
    search_fields = ['estadio', 'cidade']
    ordering_fields = ['data_hora']


class EventoJogoViewSet(viewsets.ModelViewSet):
    queryset = EventoJogo.objects.all()
    serializer_class = EventoJogoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['jogo','jogador', 'tipo']
