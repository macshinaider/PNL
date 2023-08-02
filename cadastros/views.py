from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Fisicas, Juridicas
from django.urls import reverse_lazy


# CRIANDO OS CADASTROS

class FisicasCreate(CreateView):
    model = Fisicas
    fields = ['nome','cpf', 'rg',  'nomepai', 'nomemae','nascimento', 'cidade_nascimento', 'estado_civil', 'cep', 'cidade', 'bairro', 'rua', 'numeracao', 'fone', 'tpr', 'imovel_proprio', 'valor_imovel', 'local_trabalho', 'nome_empresa', 'cep_empresa', 'cidade_empresa', 'bairro_empresa', 'rua_empresa', 'numeracao_empresa', 'tempo_servico', 'registrado', 'funcao', 'salario', 'futura_empresa', 'cep_futura_empresa', 'cidade_futura_empresa', 'bairro_futura_empresa', 'rua_futura_empresa', 'numeracao_futura_empresa', 'faturamento', 'fone_futura_empresa']
    template_name = 'cadastros/form-fisica.html'
    success_url = reverse_lazy('listas-pessoas-fisicas')


class JuridicasCreate(CreateView):
    model = Juridicas
    fields = ['nome', 'cnpj', 'cpf',]
    template_name = 'cadastros/form-juridica.html'
    success_url = reverse_lazy('listas-pessoas-juridicas')


# ATUALIZANDO OS CADASTROS

class FisicasUpdate(UpdateView):
    model = Fisicas
    fields = ['nome','cpf', 'rg',  'nomepai', 'nomemae','nascimento', 'cidade_nascimento', 'estado_civil', 'cep', 'cidade', 'bairro', 'rua', 'numeracao', 'fone', 'tpr', 'imovel_proprio', 'valor_imovel', 'local_trabalho', 'nome_empresa', 'cep_empresa', 'cidade_empresa', 'bairro_empresa', 'rua_empresa', 'numeracao_empresa', 'tempo_servico', 'registrado', 'funcao', 'salario', 'futura_empresa', 'cep_futura_empresa', 'cidade_futura_empresa', 'bairro_futura_empresa', 'rua_futura_empresa', 'numeracao_futura_empresa', 'faturamento', 'fone_futura_empresa']
    template_name = 'cadastros/form-fisica.html'
    success_url = reverse_lazy('listas-pessoas-fisicas')


class JuridicasUpdate(UpdateView):
    model = Juridicas
    fields = ['nome', 'cnpj', 'cpf',]
    template_name = 'cadastros/form-juridica.html'
    success_url = reverse_lazy('listas-pessoas-juridicas')


# DELETANDO OS CADASTROS

class FisicasDelete(DeleteView):
    model = Fisicas
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listas-pessoas-fisicas')


class JuridicasDelete(DeleteView):
    model = Juridicas
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listas-pessoas-juridicas')


# LISTANDO OS CADASTROS

class FisicasList(ListView):
    model = Fisicas
    template_name = 'cadastros/listas/fisicas.html'


class JuridicasList(ListView):
    model = Juridicas
    template_name = 'cadastros/listas/juridicas.html'