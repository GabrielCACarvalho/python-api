from rest_framework import viewsets, generics
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


class ListaPedidosCliente(generics.ListAPIView):
    """Listando os pedidos de um cliente"""
    def get_queryset(self):
        queryset = Pedido.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPedidosClienteSerializer


class ListaProdutosCategoria(generics.ListAPIView):
    """Listando os produtos de uma categoria"""
    def get_queryset(self):
        queryset = Produto.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaProdutosCategoriaSerializer


#class ListarPedidosStatus(generics.ListAPIView):
    #"""Listando os pedidos de um status"""
    #def get_queryset(self):
        #queryset = Pedido.objects.filter(categoria_id=self.kwargs['pk'])
        #return queryset
    #serializer_class = ListaProdutosCategoriaSerializer



class ListaProdutosMarca(generics.ListAPIView):
    """Listando os produtos de uma marca"""
    def get_queryset(self):
        queryset = Produto.objects.filter(marca_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaProdutosMarcaSerializer


class ListaProdutosPromocao(generics.ListAPIView):
    """Listando os produtos de uma promoção"""
    def get_queryset(self):
        queryset = Produto.objects.filter(promocao_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaProdutosPromocaoSerializer


class ListaItensPedido(generics.ListAPIView):
    """Listando os itens de um pedido"""
    def get_queryset(self):
        queryset = Item.objects.filter(pedido=self.kwargs['pk'])
        return queryset
    serializer_class = ListaItensPedidoSerializer


class ListaEnderecosCliente(generics.ListAPIView):
    """Listando os endereços de um cliente"""
    def get_queryset(self):
        queryset = Endereco.objects.filter(cliente=self.kwargs['pk'])
        return queryset
    serializer_class = ListaEnderecosClienteSerializer