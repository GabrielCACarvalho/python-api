from django.db import models


class Endereco(models.Model):
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)

    def __str__(self):
        return self.cep


class Cliente(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False, null=False)
    senha = models.CharField(max_length=20)  # TODO: verificar se vai ficar assim
    celular = models.CharField(max_length=11)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    data_cadastro = models.DateField()

    def __str__(self):
        return self.cpf


class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Promocao(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    porcentagem_desconto = models.DecimalField(decimal_places=2, max_digits=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    valor_unitario = models.DecimalField(decimal_places=2, max_digits=50)
    estoque = models.IntegerField()
    quantidade = models.IntegerField()
    promocao = models.ForeignKey(Promocao, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS = (
        ('Solicitado', 'O pedido foi solicitado, mas não confirmado.'),
        ('Confirmado', 'O pedido foi confirmado, aguardando o pagamento.'),
        ('Pago', 'O pedido foi pago, agora será postado.'),
        ('Aguardando envio', 'O pedido foi postado, agora está aguardando envio.'),
        ('Enviado', 'O pedido Foi enviado, aguardando a confirmação de recebimento do cliente.'),
        ('Entregue', 'O cliente recebeu o pedido.'),
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField()
    data_pagamento = models.DateField()
    data_envio = models.DateField()
    forma_pagamento = models.CharField(max_length=100)
    status_pedido = models.CharField(max_length=100, choices=STATUS, blank=False, null=False, default='Solicitado')
    valor_total = models.DecimalField(decimal_places=2, max_digits=50)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

    def __str__(self):
        self.cliente
