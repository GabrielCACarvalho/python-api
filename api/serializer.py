from rest_framework import serializers
from api.models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'email', 'sexo', 'celular', 'endereco', 'data_cadastro']


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nome']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']


class PromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocao
        fields = ['id', 'nome', 'data_inicio', 'data_fim', 'porcentagem_desconto']


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'marca', 'categoria', 'valor_unitario', 'promocao']


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'data_criacao', 'data_pagamento', 'data_envio', 'forma_pagamento', 'status_pedido', 'valor_total', 'item']


class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = GerenciamentoEstoque
        fields = ['id', 'produto', 'itens_em_estoque']


class ListaPedidosClienteSerializer(serializers.ModelSerializer):
    item = serializers.ReadOnlyField(source='item.produto.nome')

    class Meta:
        model = Pedido
        fields = ['status_pedido', 'item']


class ListaProdutosCategoriaSerializer(serializers.ModelSerializer):
    marca = serializers.ReadOnlyField(source='marca.nome')

    class Meta:
        model = Produto
        fields = ['nome', 'marca']


#class ListaPedidosStatusSerializer(serializers.ModelSerializer):
    #item = serializers.ReadOnlyField(source='item.produto.nome')

    #class Meta:
        #model = Pedido
        #fields = ['status_pedido', 'item']


class ListaProdutosMarcaSerializer(serializers.ModelSerializer):
    marca = serializers.ReadOnlyField(source='marca.nome')

    class Meta:
        model = Produto
        fields = ['nome', 'marca']


class ListaProdutosPromocaoSerializer(serializers.ModelSerializer):
    promocao = serializers.ReadOnlyField(source='promocao.nome')

    class Meta:
        model = Produto
        fields = ['nome', 'promocao']


class ListaItensPedidoSerializer(serializers.ModelSerializer):
    produto = serializers.ReadOnlyField(source='produto.nome')

    class Meta:
        model = Item
        fields = ['produto', 'quantidade', 'valor_total']


class ListaEnderecosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['estado', 'cidade', 'bairro']