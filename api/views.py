from rest_framework import viewsets
from api.models import *
from api.serializer import *

class ClienteViewSet(viewsets.ModelViewSet):
    """Exibindo os Clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as marcas"""
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """Exibindo todas ascategorias"""
    queryset = Categoria.objects.all()
    serializer_class = ClienteSerializer


class PromocaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as promoções"""
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Produto.objects.all()
    serializer_class = PromocaoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    """Exibindo os pedidos"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class EstoqueViewSet(viewsets.ModelViewSet):
    """Exibindo o estoque"""
    queryset = GerenciamentoEstoque.objects.all()
    serializer_class = EstoqueSerializer
