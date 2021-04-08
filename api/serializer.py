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