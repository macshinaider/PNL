from django.db import models

# Create your models here.
class Fisicas(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.FloatField(max_length=11)
    rg = models.FloatField(max_length=8)
    nomepai = models.CharField(max_length=100)
    nomemae = models.CharField(max_length=100)
    nascimento = models.DateField('data', null=True, blank=True)
    cidade_nascimento = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=3)
    cep = models.IntegerField(verbose_name="Cep atual")
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numeracao = models.IntegerField(verbose_name="Número da casa")
    fone = models.IntegerField(verbose_name="Número de telefone")
    tpr = models.CharField(max_length=50 ,verbose_name="Tempo de residência")
    imovel_proprio = models.CharField(max_length=3)
    valor_imovel = models.FloatField(verbose_name="Valor do imóvel")
    local_trabalho = models.CharField(max_length=50 ,verbose_name="Local de trabalho atual")
    nome_empresa = models.CharField(max_length=50 ,verbose_name="Nome da empresa")
    cep_empresa = models.IntegerField(verbose_name="Cep da empresa atual")
    cidade_empresa = models.CharField(max_length=50)
    bairro_empresa = models.CharField(max_length=50)
    rua_empresa = models.CharField(max_length=50)
    numeracao_empresa = models.IntegerField(verbose_name="Número da empresa")
    tempo_servico = models.IntegerField(verbose_name="Tempo de serviço prestado")
    registrado = models.CharField(max_length=3)
    funcao = models.CharField(max_length=50,verbose_name="Função na empresa")
    salario = models.FloatField(verbose_name="Salario")
    futura_empresa = models.CharField(max_length=50 ,verbose_name="Nome da futura empresa")
    cep_futura_empresa = models.IntegerField(verbose_name="Cep da futura empresa")
    cidade_futura_empresa = models.CharField(max_length=50)
    bairro_futura_empresa = models.CharField(max_length=50)
    rua_futura_empresa = models.CharField(max_length=50)
    numeracao_futura_empresa = models.IntegerField(verbose_name="Número da empresa")
    faturamento = models.IntegerField(verbose_name="Faturamento")
    fone_futura_empresa = models.IntegerField(verbose_name="Número de contato da Empresa")

    def __str__(self):
        return "{} ({})".format(self.nome, self.cpf)
    
class Juridicas(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.FloatField(max_length=14)
    cpf = models.FloatField(max_length=11)

    def __str__(self):
        return "{} ({})".format(self.nome, self.cnpj)