from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Fisicas, Juridicas
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin


# CRIANDO OS CADASTROS

class FisicasCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Fisicas
    fields = ['nome_fisica','cpf_fisica', 'rg_fisica',  'nomepai', 'nomemae','nascimento', 'cidade_nascimento', 'estado_civil', 'cep', 'cidade', 'bairro', 'rua', 'numeracao', 'fone', 'tpr', 'imovel_proprio', 'valor_imovel', 'local_trabalho', 'nome_empresa', 'cep_empresa', 'cidade_empresa', 'bairro_empresa', 'rua_empresa', 'numeracao_empresa', 'tempo_servico', 'registrado', 'funcao', 'salario', 'futura_empresa', 'cep_futura_empresa', 'cidade_futura_empresa', 'bairro_futura_empresa', 'rua_futura_empresa', 'numeracao_futura_empresa', 'faturamento', 'fone_futura_empresa', 'proprietario', 'nome_proprietario', 'cnpj', 'banco', 'agencia', 'ref_parente_1', 'fone_parente_1', 'ref_parente_2', 'fone_parente_2']
    template_name = 'cadastros/form-fisica.html'
    success_url = reverse_lazy('listas-pessoas-fisicas')


class JuridicasCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Juridicas
    fields = ['razao_social', 'cnpj', 'data_abertura', 'cep', 'cidade', 'bairro', 'rua', 'numero', 'nome_contador', 'fone_contador', 'email', 'faturamento', 'presta_servico', 'empresa', 'tempo_prestado', 'cep_empresa', 'cidade_empresa', 'bairro_empresa', 'rua_empresa', 'numero_empresa', 'banco', 'agencia']
    template_name = 'cadastros/form-juridica.html'
    success_url = reverse_lazy('listas-pessoas-juridicas')


# ATUALIZANDO OS CADASTROS

class FisicasUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Fisicas
    fields = ['nome_fisica','cpf_fisica', 'rg_fisica',  'nomepai', 'nomemae','nascimento', 'cidade_nascimento', 'estado_civil', 'cep', 'cidade', 'bairro', 'rua', 'numeracao', 'fone', 'tpr', 'imovel_proprio', 'valor_imovel', 'local_trabalho', 'nome_empresa', 'cep_empresa', 'cidade_empresa', 'bairro_empresa', 'rua_empresa', 'numeracao_empresa', 'tempo_servico', 'registrado', 'funcao', 'salario', 'futura_empresa', 'cep_futura_empresa', 'cidade_futura_empresa', 'bairro_futura_empresa', 'rua_futura_empresa', 'numeracao_futura_empresa', 'faturamento', 'fone_futura_empresa', 'proprietario', 'nome_proprietario', 'cnpj', 'banco', 'agencia', 'ref_parente_1', 'fone_parente_1', 'ref_parente_2', 'fone_parente_2']
    template_name = 'cadastros/form-fisica.html'
    success_url = reverse_lazy('listas-pessoas-fisicas')


class JuridicasUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Juridicas
    fields = ['razao_social', 'cnpj', 'data_abertura', 'cep', 'cidade', 'bairro', 'rua', 'numero', 'nome_contador', 'fone_contador', 'email', 'faturamento', 'presta_servico', 'empresa', 'tempo_prestado', 'cep_empresa', 'cidade_empresa', 'bairro_empresa', 'rua_empresa', 'numero_empresa', 'banco', 'agencia']
    template_name = 'cadastros/form-juridica.html'
    success_url = reverse_lazy('listas-pessoas-juridicas')


# DELETANDO OS CADASTROS

class FisicasDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Fisicas
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listas-pessoas-fisicas')


class JuridicasDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Juridicas
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listas-pessoas-juridicas')


# LISTANDO OS CADASTROS

class FisicasList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Fisicas
    template_name = 'cadastros/listas/fisicas.html'


class JuridicasList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Juridicas
    template_name = 'cadastros/listas/juridicas.html'