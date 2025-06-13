from robot.api.deco import keyword, library
from unittest.mock import patch

@library
class ApiMockLibrary:

    @keyword
    def get_produtos_mock(self):
        return [
            {"nome": "GPU RTX 3070", "tipo": "Placa de Vídeo", "quantidade_estoque": 3},
            {"nome": "Ryzen 7", "tipo": "Processador", "quantidade_estoque": 5}
        ]

    @keyword
    def realizar_venda_mock(self, produto, quantidade):
        # Garantir que 'quantidade' seja um inteiro
        quantidade = int(quantidade)  # Conversão explícita para inteiro
        estoque = {"Ryzen 7": 5}
    
        # Comparação
        if estoque.get(produto, 0) >= quantidade:
            return {"status": 200, "mensagem": "Venda realizada com sucesso"}
        return {"status": 400, "mensagem": "Estoque insuficiente"}


    @keyword
    def get_produtos_mock(self):
        return [
            {"nome": "RTX 4060", "tipo": "placa de vídeo", "quantidade_estoque": 2, "preco": 2500.00},
            {"nome": "Ryzen 5 5600G", "tipo": "processador", "quantidade_estoque": 5, "preco": 1200.00}
        ]

    @keyword
    def realizar_venda_mock(self, nome_produto, quantidade):
        if quantidade > 5:
            return {"status": 400, "mensagem": "Estoque insuficiente"}
        return {"status": 200, "mensagem": "Venda realizada com sucesso"}

    @keyword
    def montar_computador_mock(self, nome_computador, gpu, cpu):
        return {"status": 200, "mensagem": "Computador montado com sucesso", "id": 1, "nome": nome_computador}

    @keyword
    def get_detalhes_produto_mock(self, nome_produto):
        if nome_produto == "RTX 4060":
            return {"nome": "RTX 4060", "tipo": "placa de vídeo", "preco": 2500.00, "quantidade_estoque": 2}
        return {"nome": nome_produto, "tipo": "desconhecido", "preco": 0, "quantidade_estoque": 0}

    @keyword
    def get_historico_vendas_mock(self):
        return [
            {"id_venda": 1, "produto": "Ryzen 7", "data_venda": "2025-06-13", "quantidade": 2},
            {"id_venda": 2, "produto": "RTX 4060", "data_venda": "2025-06-14", "quantidade": 1}
        ]

    @keyword
    def atualizar_quantidade_estoque_mock(self, nome_produto, nova_quantidade):
        return {"status": 200, "mensagem": "Quantidade de produto atualizada com sucesso"}
