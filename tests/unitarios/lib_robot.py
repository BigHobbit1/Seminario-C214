from app.auxiliar import (
    validar_nome, validar_preco, validar_quantidade,
    criar_produto_valido, calcular_total_estoque,
    verificar_pecas_necessarias, montar_computador,
    pode_realizar_venda, registrar_venda,
    nome_invalido, preco_invalido, quantidade_invalida,
    montar_computador_faltando_pecas, tentar_venda_sem_estoque
)

class lib_robot:
    def validar_nome(self, nome):
        return validar_nome(nome)

    def validar_preco(self, preco):
        return validar_preco(preco)

    def validar_quantidade(self, quantidade):
        return validar_quantidade(quantidade)

    def criar_produto_valido(self, nome, tipo, marca, modelo, preco, quantidade):
        return criar_produto_valido(nome, tipo, marca, modelo, preco, quantidade)

    def calcular_total_estoque(self, produtos):
        return calcular_total_estoque(produtos)

    def verificar_pecas_necessarias(self, disponiveis, necessarias):
        return verificar_pecas_necessarias(disponiveis, necessarias)

    def montar_computador(self, estoque, pecas):
        return montar_computador(estoque, pecas)

    def pode_realizar_venda(self, estoque, produto, quantidade):
        return pode_realizar_venda(estoque, produto, quantidade)

    def registrar_venda(self, estoque, produto, quantidade):
        return registrar_venda(estoque, produto, quantidade)

    def nome_invalido(self, nome):
        return nome_invalido(nome)

    def preco_invalido(self, preco):
        return preco_invalido(preco)

    def quantidade_invalida(self, quantidade):
        return quantidade_invalida(quantidade)

    def montar_computador_faltando_pecas(self, estoque, pecas):
        return montar_computador_faltando_pecas(estoque, pecas)

    def tentar_venda_sem_estoque(self, estoque, produto, quantidade):
        return tentar_venda_sem_estoque(estoque, produto, quantidade)