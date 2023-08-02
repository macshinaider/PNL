from django.urls import path


from .views import FisicasCreate, JuridicasCreate
from .views import FisicasUpdate, JuridicasUpdate
from .views import FisicasDelete, JuridicasDelete
from .views import FisicasList, JuridicasList

urlpatterns = [
    # path('endereço', minhaView.as_view(), name="nome da view")

    #Rotas das createsViews
    path('cadastrar/fisicas/', FisicasCreate.as_view(), name="cadastrar-pessoas-fisicas"),
    path('cadastrar/juridicas/', JuridicasCreate.as_view(), name="cadastrar-pessoas-juridicas"),

    #Rotas das UpdatesViews
    path('atualizar/pessoa-fisica/<int:pk>', FisicasUpdate.as_view(), name="atualizar-pessoa-fisica"),
    path('atualizar/pessoa-juridicas/<int:pk>', JuridicasUpdate.as_view(), name="atualizar-pessoa-juridica"),

    #Rotas das deletesViews
    path('excluir/pessoa-fisica/<int:pk>', FisicasDelete.as_view(), name="excluir-pessoa-fisica"),
    path('excluir/pessoa-juridica/<int:pk>', JuridicasDelete.as_view(), name="excluir-pessoa-juridica"),

    #Rotas das ListViews
    path('lista/fisicas/', FisicasList.as_view(), name="listas-pessoas-fisicas"),
    path('lista/juridicas/', JuridicasList.as_view(), name="listas-pessoas-juridicas")
]