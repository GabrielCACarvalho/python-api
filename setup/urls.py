from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Clientes') # TODO: verificar se tem necessidade de ver todos os pedidos
router.register('pedidos', PedidoViewSet, basename='Pedidos') # TODO: verificar se tem necessidade de ver todos os clientes
router.register('estoque', EstoqueViewSet, basename='Estoque')
router.register('categorias', CategoriaViewSet, basename='Categorias')
router.register('promocoes', PromocaoViewSet, basename='Promoções')
router.register('produtos', ProdutoViewSet, basename='Produtos') # TODO: verificar se tem necessidade de ver todos os produtos
router.register('marcas', MarcaViewSet, basename="Marcas")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
