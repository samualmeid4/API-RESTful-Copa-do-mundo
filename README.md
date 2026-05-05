# API-RESTful-Copa-do-mundo
Atividade Prática de Programação com Banco de Dados





from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Grupo(models.Model):
    nome = models.CharField(max_length=1)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"Grupo {self.nome}"
    

class Tecnico(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=100)
    data_nasc = models.DateField()

    def __str__(self):
        return f"Técnico {self.nome}"

class Selecao(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3, unique=True) 

    confederacao = [
        ('AFG', 'Afeganistão'), ('RSA', 'África do Sul'), ('ALB', 'Albânia'),
        ('GER', 'Alemanha'), ('ANG', 'Angola'), ('KSA', 'Arábia Saudita'),
        ('ALG', 'Argélia'), ('ARG', 'Argentina'), ('AUS', 'Austrália'),
        ('AUT', 'Áustria'), ('BEL', 'Bélgica'), ('BOL', 'Bolívia'),
        ('BIH', 'Bósnia e Herzegovina'), ('BRA', 'Brasil'), ('CAN', 'Canadá'),
        ('QAT', 'Catar'), ('CHI', 'Chile'), ('CHN', 'China'),
        ('COL', 'Colômbia'), ('KOR', 'Coreia do Sul'), ('CIV', 'Costa do Marfim'),
        ('CRC', 'Costa Rica'), ('CRO', 'Croácia'), ('DEN', 'Dinamarca'),
        ('EGY', 'Egito'), ('ECU', 'Equador'), ('SCO', 'Escócia'),
        ('SVK', 'Eslováquia'), ('SLO', 'Eslovênia'), ('ESP', 'Espanha'),
        ('USA', 'Estados Unidos'), ('FRA', 'França'), ('GHA', 'Gana'),
        ('GRE', 'Grécia'), ('NED', 'Holanda'), ('HON', 'Honduras'),
        ('HUN', 'Hungria'), ('ENG', 'Inglaterra'), ('IRN', 'Irã'),
        ('IRQ', 'Iraque'), ('IRL', 'Irlanda'), ('ISL', 'Islândia'),
        ('ITA', 'Itália'), ('JAM', 'Jamaica'), ('JPN', 'Japão'),
        ('MAR', 'Marrocos'), ('MEX', 'México'), ('NGA', 'Nigéria'),
        ('NOR', 'Noruega'), ('NZL', 'Nova Zelândia'), ('PAN', 'Panamá'),
        ('PAR', 'Paraguai'), ('PER', 'Peru'), ('POL', 'Polônia'),
        ('POR', 'Portugal'), ('CZE', 'República Tcheca'), ('ROU', 'Romênia'),
        ('RUS', 'Rússia'), ('SEN', 'Senegal'), ('SRB', 'Sérvia'),
        ('SWE', 'Suécia'), ('SUI', 'Suíça'), ('TUN', 'Tunísia'),
        ('TUR', 'Turquia'), ('UKR', 'Ucrânia'), ('URU', 'Uruguai'),
        ('UZB', 'Uzbequistão'), ('VEN', 'Venezuela'),
    ]

    grupo = models.ForeignKey(Grupo, on_delete=PROTECT, related_name='selecoes')
    tecnico = models.OneToOneField(Tecnico, on_delete=SET_NULL, null=True,related_name='selecao')

    escudo = models.URLField(blank=True) 

    def __str__(self):
        return f"Seleção in {self.nome}"



class Jogador(models.Model):
    nome = models.CharField(max_length=150)
    nome_guerra = models.CharField(max_length=50) 
    selecao = models.ForeignKey(Selecao, on_delete=PROTECT, related_name='jogadores')
    posicao = [
        ('Goleiro', 'GL'),
        ('Zagueiro', 'ZAG'),
        ('Lateral', 'LA'),
        ('Volante', 'VOL'),
        ('Meia', 'MC'),
        ('Atacante', 'ATA')

    ]
    numero_camisa = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(26)
        ],
        help_text="Insira um valor entre 1 e 26"
    )
    data_nasc = models.DateField()
    suspenso = models.BooleanField(default=False)

class Jogo(models.Model):
    selecao_mandante = models.ForeignKey(Selecao, related_name='jogos_mandante', on_delete=PROTECT)
    selecao_visitante = models.ForeignKey(Selecao, related_name='jogos_visitante', on_delete=PROTECT)

    fase = [
        ('Grupos'),
        ('Fase 32'),
        ('Oitavas'),
        ('Quartas'),
        ('Semifinal'),
        ('Final')
    ]
    grupo = models.ForeignKey(Grupo, on_delete=PROTECT, null=True, blank=True)
    data_hora = models.DateTimeField()
    estadio = models.CharField(max_length=150, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    gols_mandante = models.PositiveSmallIntegerField(default=0)
    gols_visitante = models.PositiveSmallIntegerField(default=0)
    status = [
        ('Agendado'),
        ('Em_andamento'),
        ('Encerrado'),
        ('Cancelado')
    ]

class eventos(models.Model):
    eventos = 

class EventoJogo(models.Model):
    Jogo = models.ForeignKey(Jogo, on_delete=CASCADE,related_name='eventos')
    Jogador = models.ForeignKey(Jogador, on_delete=PROTECT, related_name='eventos')
    tipo = [
        ('Gol'),
        ('Cartao_amarelo'),
        ('Cartao_vermelho'),
        ('Gol_contra')
    ]
    minuto = models.PositiveSmallIntegerField()
    acressimo = models.BooleanField(default=False)
    

