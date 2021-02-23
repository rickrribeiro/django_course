from django.db import models

class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Qt estoque')

    #retorna a representação de string do objeto
    def __str__(self):
        return f'{self.nome}-{self.estoque}'

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    linguagem = models.CharField('Linguagem', max_length=100)
    descricao = models.CharField('Descrição', max_length=100)
    def __str__(self):
        return self.nome