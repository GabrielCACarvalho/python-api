from django.contrib import admin
from api.models import *


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'sexo', 'celular', 'endereco', 'data_cadastro')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20


admin.site.register(Cliente, Clientes)


class Enderecos(admin.ModelAdmin):
    list_display = ('id', 'estado', 'cidade', 'bairro', 'cep', 'rua', 'numero')
    list_display_links = ('cep',)
    search_fields = ('cep',)
    list_per_page = 20


admin.site.register(Endereco, Enderecos)


class Marcas(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_fields = ('id',)
    list_per_page = 20


admin.site.register(Marca, Marcas)


class Categorias(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_fields = ('id',)
    list_per_page = 20


admin.site.register(Categoria, Categorias)


class Promocoes(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim', 'porcentagem_desconto')
    list_display_links = ('nome',)
    search_fields = ('id',)
    list_per_page = 20


admin.site.register(Promocao, Promocoes)


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'marca', 'categoria', 'valor_unitario', 'estoque', 'quantidade')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Produto, Produtos)


class Pedidos(admin.ModelAdmin):
    list_display = (
    'id', 'cliente', 'data_criacao', 'data_pagamento', 'data_envio', 'forma_pagamento', 'status_pedido', 'valor_total')
    list_display_links = ('id',)
    search_fields = ('id', 'status_pedido')
    list_per_page = 20


admin.site.register(Pedido, Pedidos)
