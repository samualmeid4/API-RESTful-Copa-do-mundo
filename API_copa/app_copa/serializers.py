from rest_framework import serializers
from .models import Grupo, Tecnico, Selecao, Jogador, Jogo, EventoJogo
#------------------------------------------------------------------------

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'



class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'



class SelecaoSerializer(serializers.ModelSerializer):
    nome_tecnico = serializers.CharField(source='tecnico.nome', read_only=True)

    class Meta:
        model = Selecao
        fields = '__all__'



class JogadorSerializer(serializers.ModelSerializer):
    jogador = serializers.CharField(source='get_posicao_display', read_only=True)

    class Meta:
        model = Jogador
        fields = '__all__'



class EventoJogoSerializer(serializers.ModelSerializer):
    jogador_nome = serializers.CharField(source='jogador.nome_guerra', read_only=True)
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)

    class Meta:
        model = EventoJogo
        fields = '__all__'



class JogoSerializer(serializers.ModelSerializer):
    nome_mandante = serializers.CharField(source='selecao_mandante.nome', read_only=True)
    nome_visitante = serializers.CharField(source='selecao_visitante.nome', read_only=True)
    fase_display = serializers.CharField(source='get_fase_display', read_only=True)

    eventos = EventoJogoSerializer(many=True, read_only=True)

    resultado = serializers.SerializerMethodField()

    class Meta:
        model = Jogo
        fields = '__all__'

    def get_resultado(self, obj):
        if obj.gols_mandante > obj.gols_visitante:
            return 'Mandante venceu'
        elif obj.gols_visitante > obj.gols_mandante:
            return 'Visitante venceu'
        return 'Empate'
    

    def create(self, validated_data):
        eventos_data = validated_data.pop('eventos',[])
        jogo = Jogo.objects.create(**validated_data)

        for evento_data in eventos_data:
            EventoJogo.objects.create(jogo=jogo, **evento_data)
        return jogo

    
 