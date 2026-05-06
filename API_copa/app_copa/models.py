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

    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, related_name='selecoes')
    tecnico = models.OneToOneField(Tecnico, on_delete=models.SET_NULL, null=True,related_name='selecao')

    escudo = models.URLField(blank=True) 

    def __str__(self):
        return f"Seleção in {self.nome}"



class Jogador(models.Model):
    nome = models.CharField(max_length=150)
    nome_guerra = models.CharField(max_length=50) 
    selecao = models.ForeignKey(Selecao, on_delete=models.PROTECT, related_name='jogadores')
    posicao_choices = [
        ('GL','Goleiro'),
        ('ZAG', 'Zagueiro'),
        ('LAT', 'Lateral'),
        ('VOL', 'Volante'),
        ('MC', 'Meia'),
        ('ATA', 'Atacante')

    ]
    numero_camisa = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(26)
        ],
        help_text="Insira um valor entre 1 e 26"
    )

    posicao = models.CharField(max_length=3, choices=posicao_choices)
    data_nasc = models.DateField()
    suspenso = models.BooleanField(default=False)

class Jogo(models.Model):
    selecao_mandante = models.ForeignKey(Selecao, related_name='jogos_mandante', on_delete=models.PROTECT)
    selecao_visitante = models.ForeignKey(Selecao, related_name='jogos_visitante', on_delete=models.PROTECT)

    fase_choices = [
        ('Grupos', 'Grupos'),
        ('Fase 32', 'Fase 32'),
        ('Oitavas', 'Oitavas'),
        ('Quartas', 'Quartas'),
        ('Semifinal', 'Semifinal'),
        ('Final', 'Final')
    ]
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, null=True, blank=True)
    data_hora = models.DateTimeField()
    estadio = models.CharField(max_length=150, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    gols_mandante = models.PositiveSmallIntegerField(default=0)
    gols_visitante = models.PositiveSmallIntegerField(default=0)
    status_choices = [
        ('Agendado', 'Agendado'),
        ('Em_andamento', 'Em Andamento'),
        ('Encerrado', 'Encerrado'),
        ('Cancelado', 'Cancelado')
    ]

    fase = models.CharField(max_length=20, choices=fase_choices)
    status = models.CharField(max_length=20, choices=status_choices, default='Agendado')

class EventoJogo(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE,related_name='eventos')
    jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT, related_name='eventos')
    tipo_choices = [
        ('Gol', 'Gol'),
        ('Cartao_amarelo', 'Cartão Amarelo'),
        ('Cartao_vermelho', 'Cartão Vermelho'),
        ('Gol_contra', 'Gol Contra')
    ]
    minuto = models.PositiveSmallIntegerField()
    tipo = models.CharField(max_length=20, choices=tipo_choices)
    acressimo = models.BooleanField(default=False)
    

