from django.db import models

# Create your models here.
class Fisicas(models.Model):
    nome_fisica = models.CharField(max_length=100, verbose_name="Nome completo")
    cpf_fisica = models.FloatField(verbose_name="CPF")
    rg_fisica = models.FloatField(verbose_name="RG")
    nascimento = models.DateField('data de nascimento')
    nomepai = models.CharField(max_length=100, verbose_name="Nome do pai")
    nomemae = models.CharField(max_length=100, verbose_name="Nome da mãe")
    cidade_nascimento = models.CharField(max_length=100, verbose_name="Natural de")
    estado_civil = models.CharField(max_length=100)
    cep = models.FloatField(verbose_name="Cep atual")
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numeracao = models.FloatField(verbose_name="Número da casa")
    fone = models.FloatField(verbose_name="Número de telefone")
    tpr = models.CharField(max_length=100 ,verbose_name="Tempo de residência")
    imovel_proprio = models.CharField(max_length=100, verbose_name="Imóvel Proprio")
    valor_imovel = models.FloatField(verbose_name="Valor do imóvel")
    local_trabalho = models.CharField(max_length=100 ,verbose_name="Local de trabalho atual")
    nome_empresa = models.CharField(max_length=100 ,verbose_name="Nome da empresa")
    cep_empresa = models.FloatField(verbose_name="Cep da empresa atual")
    cidade_empresa = models.CharField(max_length=100)
    bairro_empresa = models.CharField(max_length=100)
    rua_empresa = models.CharField(max_length=100)
    numeracao_empresa = models.FloatField(verbose_name="Número da empresa")
    tempo_servico = models.FloatField(verbose_name="Tempo de serviço prestado")
    registrado = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100,verbose_name="Função na empresa")
    salario = models.FloatField(verbose_name="Salario")
    futura_empresa = models.CharField(max_length=100 ,verbose_name="Nome da futura empresa")
    cep_futura_empresa = models.FloatField(verbose_name="Cep da futura empresa")
    cidade_futura_empresa = models.CharField(max_length=100)
    bairro_futura_empresa = models.CharField(max_length=100)
    rua_futura_empresa = models.CharField(max_length=100)
    numeracao_futura_empresa = models.FloatField(verbose_name="Número da empresa")
    faturamento = models.FloatField(verbose_name="Faturamento")
    fone_futura_empresa = models.FloatField(verbose_name="Número de contato da Empresa")
    proprietario = models.CharField(max_length=100 ,verbose_name="Proprietario da empresa")
    nome_proprietario = models.CharField(max_length=100, verbose_name="Nome completo")
    cnpj = models.FloatField(verbose_name="CNPJ")
    banco = models.CharField(max_length=100)
    agencia = models.FloatField(verbose_name="Número da agencia")
    ref_parente_1 = models.CharField(max_length=100, verbose_name="Referência parentesca")
    fone_parente_1 = models.FloatField(verbose_name="Número para contato")
    ref_parente_2 = models.CharField(max_length=100, verbose_name="Referência parentesca")
    fone_parente_2 = models.FloatField(verbose_name="Número para contato")
    


    def __str__(self):
        return "{} ({})".format(self.nome, self.cpf)
    
class Juridicas(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.FloatField(max_length=14)
    data_abertura = models.DateField('data de abertura')
    cep = models.FloatField(verbose_name="CEP")
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.FloatField(verbose_name="Número para contato")
    nome_contador = models.CharField(max_length=100, verbose_name="Nome do contador")
    fone_contador = models.FloatField(verbose_name="Número do contador")
    email = models.EmailField(max_length=250)
    faturamento = models.FloatField(verbose_name="Faturamento")
    presta_servico = models.CharField(max_length=100, verbose_name="Presta serviço a")
    empresa = models.CharField(max_length=100)
    tempo_prestado = models.FloatField(verbose_name="Tempo de serviço prestado")
    cep_empresa = models.FloatField(verbose_name="CEP EMPRESA")
    cidade_empresa = models.CharField(max_length=100, verbose_name="Cidade")
    bairro_empresa = models.CharField(max_length=100, verbose_name="Nome do bairro da empresa")
    rua_empresa = models.CharField(max_length=100, verbose_name="Nome da rua da empresa")
    numero_empresa = models.IntegerField(verbose_name="Númeração da empresa")
    banco = models.CharField(max_length=100)
    agencia = models.IntegerField(verbose_name="Agencia")



    def __str__(self):
        return "{} ({})".format(self.nome, self.cnpj)