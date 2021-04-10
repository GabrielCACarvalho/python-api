from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('estoque', EstoqueViewSet, basename='Estoque')
router.register('categorias', CategoriaViewSet, basename='Categorias')
router.register('promocoes', PromocaoViewSet, basename='Promoções')
router.register('marcas', MarcaViewSet, basename="Marcas")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('pedidos/<int:pk>/cliente/', ListaPedidosCliente.as_view()),
    path('categorias/<int:pk>/produtos/', ListaProdutosCategoria.as_view()),
    path('marcas/<int:pk>/produtos/', ListaProdutosMarca.as_view()),
    path('promocaos/<int:pk>/produtos/', ListaProdutosPromocao.as_view()),
    path('pedidos/<int:pk>/itens/', ListaItensPedido.as_view()),
    path('clientes/<int:pk>/enderecos/', ListaEnderecosCliente.as_view()),
]
