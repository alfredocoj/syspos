# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.db import models

class Alunos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80L)
    dt_nascimento = models.DateField()
    cpf = models.CharField(max_length=15L)
    rg = models.CharField(max_length=15L)
    dt_emissao_rg = models.DateField()
    uf_emissao_rg = models.CharField(max_length=45L)
    endereco = models.CharField(max_length=60L)
    complemento = models.CharField(max_length=50L, blank=True)
    numero = models.CharField(max_length=20L)
    bairro = models.CharField(max_length=45L)
    cep = models.CharField(max_length=10L)
    cidades = models.ForeignKey('Cidades')
    telefone1 = models.CharField(max_length=12L)
    telefone2 = models.CharField(max_length=12L, blank=True)
    telefone3 = models.CharField(max_length=12L, blank=True)
    telefone4 = models.CharField(max_length=12L, blank=True)
    email1 = models.CharField(max_length=100L)
    email2 = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'alunos'
    def __unicode__(self):
        return u'%s' % (self.nome)
    def get_absolute_url(self):
        #return '/academico/alunos/%d/editar'%self.id
        return '/academico/alunos'

class Areas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45L)
    cursos = models.ForeignKey('Cursos')
    class Meta:
        db_table = 'areas'
    def __unicode__(self):
        return u'%s' % (self.nome)
    def get_absolute_url(self):
        return '#'

class Cidades(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80L)
    uf = models.CharField(max_length=2L)
    class Meta:
        db_table = 'cidades'
    def __unicode__(self):
        return u'%s' % (self.nome)

class Curriculos(models.Model):
    id = models.AutoField(primary_key=True)
    cursos = models.ForeignKey('Cursos')
    areas = models.ForeignKey(Areas)
    descricao = models.CharField(max_length=45L)
    class Meta:
        db_table = 'curriculos'
    def __unicode__(self):
        return u'%s' % (self.descricao)
    def get_absolute_url(self):
        return '#'

class Cursos(models.Model):
    TIPO_NENHUM = 1
    TIPO_LATO = 2
    TIPO_STRICTO = 3
    OPCOES_TIPO = (
            (TIPO_NENHUM, 'Nenhum'),
            (TIPO_LATO, 'Lato Sensu'),
            (TIPO_STRICTO, 'Stricto Sensu'),
        )
    NIVEL_APERFEICOAMENTO = 1
    NIVEL_ESPECIALIZACAO = 2
    NIVEL_MESTRADO = 3
    NIVEL_DOUTORADO = 4
    OPCOES_NIVEL = (
            (NIVEL_APERFEICOAMENTO, 'Aperfeicoamento'),
            (NIVEL_ESPECIALIZACAO, 'Especializacao'),
            (NIVEL_MESTRADO, 'Mestrado'),
            (NIVEL_DOUTORADO, 'Doutorado'),
        )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60L)
    ch = models.IntegerField(null=True, blank=True)
    #tipo = models.CharField(max_length=13L, blank=True)
    tipo = models.IntegerField(choices=OPCOES_TIPO, default=TIPO_NENHUM)
    #nivel = models.CharField(max_length=15L, blank=True)
    nivel = models.IntegerField(choices=OPCOES_NIVEL, default=NIVEL_APERFEICOAMENTO)
    dt_inicio = models.DateField()
    dt_fim = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'cursos'
    def __unicode__(self):
        return u'%s' % (self.nome)
    def get_absolute_url(self):
        #return '/academico/cursos/%d/editar'%self.id
        return '/academico/cursos'

class Disciplinas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80L)
    ch = models.IntegerField(null=True, blank=True)
    TIPO_OBRIGATORIA = 1
    TIPO_ELETIVA = 2
    OPCOES_TIPO = (
            (TIPO_OBRIGATORIA, 'Obrigatoria'),
            (TIPO_ELETIVA, 'Eletiva'),
        )
    #tipo = models.CharField(max_length=11L, blank=True)
    tipo = models.IntegerField(choices=OPCOES_TIPO, default=TIPO_OBRIGATORIA)
    ementa = models.TextField()
    programa = models.TextField(blank=True)
    cursos = models.ForeignKey(Cursos)
    class Meta:
        db_table = 'disciplinas'
    def __unicode__(self):
        return u'%s' % (self.nome)
    def get_absolute_url(self):
        return '#'

class Grade(models.Model):
    curriculos = models.AutoField(primary_key=True)
    disciplinas = models.ForeignKey(Disciplinas)
    TIPO_OBRIGATORIA = 1
    TIPO_ELETIVA = 2
    OPCOES_TIPO = (
            (TIPO_OBRIGATORIA, 'Obrigatoria'),
            (TIPO_ELETIVA, 'Eletiva'),
        )
    #tipo = models.CharField(max_length=11L)
    tipo = models.IntegerField(choices=OPCOES_TIPO, default=TIPO_OBRIGATORIA)
    class Meta:
        db_table = 'grade'
    def __unicode__(self):
        return u'%s' % (self.tipo)

class Matriculas(models.Model):
    SITUACAO_CURSANDO = 1
    SITUACAO_TRANCOU = 2
    SITUACAO_ABANDONOU = 3
    SITUACAO_DESLIGADO = 4
    SITUACAO_FORMADO = 5
    OPCOES_SITUACAO = (
            (SITUACAO_CURSANDO, 'Cursando'),
            (SITUACAO_TRANCOU, 'Trancou'),
            (SITUACAO_ABANDONOU, 'Abandonou'),
            (SITUACAO_DESLIGADO, 'Desligado'),
            (SITUACAO_FORMADO, 'Formado'),
        )
    id = models.AutoField(primary_key=True)
    alunos = models.ForeignKey(Alunos)
    cursos = models.ForeignKey(Cursos)
    matricula = models.CharField(max_length=20L, blank=True)
    dt_matricula = models.DateField()
    dt_regular = models.DateField(null=True, blank=True)
    dt_formatura = models.DateField(null=True, blank=True)
    situacao = models.IntegerField(choices=OPCOES_SITUACAO, default=SITUACAO_CURSANDO)
    class Meta:
        db_table = 'matriculas'
    def __unicode__(self):
        return u'%s' % (self.matricula)

class Ofertas(models.Model):
    id = models.AutoField(primary_key=True)
    professores = models.ForeignKey('Professores')
    semestres = models.ForeignKey('PeriodosLetivos')
    disciplinas = models.ForeignKey(Disciplinas)
    qtd_maxima = models.IntegerField()
    programa = models.TextField(blank=True)
    class Meta:
        db_table = 'ofertas'

class PeriodosLetivos(models.Model):
    id = models.AutoField(primary_key=True)
    ano = models.CharField(max_length=4L)
    semestre = models.CharField(max_length=8L)
    cursos = models.ForeignKey(Cursos)
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    prazos_entregas = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'periodos_letivos'

class Professores(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80L)
    dt_nascimento = models.DateField()
    cpf = models.CharField(max_length=15L)
    rg = models.CharField(max_length=15L)
    dt_emissao_rg = models.DateField()
    uf_emissao_rg = models.CharField(max_length=45L)
    endereco = models.CharField(max_length=60L)
    complemento = models.CharField(max_length=50L, blank=True)
    numero = models.CharField(max_length=20L)
    bairro = models.CharField(max_length=45L)
    cep = models.CharField(max_length=10L)
    cidades = models.ForeignKey(Cidades)
    telefone1 = models.CharField(max_length=12L)
    telefone2 = models.CharField(max_length=12L, blank=True)
    telefone3 = models.CharField(max_length=12L, blank=True)
    telefone4 = models.CharField(max_length=12L, blank=True)
    email1 = models.CharField(max_length=100L)
    email2 = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'professores'
    def __unicode__(self):
        return u'%s' % (self.nome)
    def get_absolute_url(self):
        #return '/academico/professores/%d/editar'%self.id
        return '/academico/professores'

class Registros(models.Model):
    id = models.AutoField(primary_key=True)
    matriculas = models.ForeignKey(Matriculas)
    ofertas = models.ForeignKey(Ofertas)
    situacao = models.CharField(max_length=8L, blank=True)
    nota = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    conceito = models.CharField(max_length=1L, blank=True)
    faltas = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'registros'

class Turmas(models.Model):
    id = models.AutoField(primary_key=True)
    ano = models.CharField(max_length=4L)
    SEMESTRE_PRIMEIRO = 1
    SEMESTRE_SEGUNDO = 2
    OPCOES_SEMESTRE = (
            (SEMESTRE_PRIMEIRO, 'Primeiro'),
            (SEMESTRE_SEGUNDO, 'Segundo'),
        )    
    #semestre = models.CharField(max_length=8L)
    semestre = models.IntegerField(choices=OPCOES_SEMESTRE, default=SEMESTRE_PRIMEIRO)
    cursos = models.ForeignKey(Cursos)
    curriculos = models.ForeignKey(Curriculos)
    class Meta:
        db_table = 'turmas'
        ordering = ['-ano']
    def __unicode__(self):
        return u'%s' % (self.nome)
    def get_absolute_url(self):
        return '#'
