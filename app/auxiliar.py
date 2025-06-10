from typing import List, Dict

# ===== Validação de Dados =====
def validar_nome(nome: str) -> bool:
    return isinstance(nome, str) and len(nome.strip()) > 0

def validar_preco(preco: float) -> bool:
    return isinstance(preco, (int, float)) and preco >= 0

def validar_quantidade(quantidade: int) -> bool:
    return isinstance(quantidade, int) and quantidade >= 0

# ===== Produtos =====
def criar_produto_valido(nome: str, tipo: str, marca: str, modelo: str, preco: float, quantidade: int) -> bool:
    return all([
        validar_nome(nome),
        validar_nome(tipo),
        validar_nome(marca),
        validar_nome(modelo),
        validar_preco(preco),
        validar_quantidade(quantidade)
    ])

def calcular_total_estoque(produtos: List[Dict]) -> int:
    return sum(produto.get("quantidade_estoque", 0) for produto in produtos)

# ===== Montagem de Computador =====
def verificar_pecas_necessarias(disponiveis: List[str], necessarias: List[str]) -> bool:
    return all(peca in disponiveis for peca in necessarias)

def montar_computador(estoque: Dict[str, int], pecas: List[str]) -> bool:
    for peca in pecas:
        if estoque.get(peca, 0) <= 0:
            return False
    return True

# ===== Vendas =====
def pode_realizar_venda(estoque: Dict[str, int], produto: str, quantidade: int) -> bool:
    return estoque.get(produto, 0) >= quantidade

def registrar_venda(estoque: Dict[str, int], produto: str, quantidade: int) -> Dict[str, int]:
    if not pode_realizar_venda(estoque, produto, quantidade):
        raise ValueError("Estoque insuficiente para a venda.")
    estoque[produto] -= quantidade
    return estoque

# ===== Funções Negativas Auxiliares para Testes =====
def nome_invalido(nome: str) -> bool:
    return not isinstance(nome, str) or nome.strip() == ""

def preco_invalido(preco) -> bool:
    return not isinstance(preco, (int, float)) or preco < 0

def quantidade_invalida(quantidade) -> bool:
    return not isinstance(quantidade, int) or quantidade < 0

def montar_computador_faltando_pecas(estoque: Dict[str, int], pecas: List[str]) -> bool:
    return any(estoque.get(peca, 0) <= 0 for peca in pecas)

def tentar_venda_sem_estoque(estoque: Dict[str, int], produto: str, quantidade: int) -> bool:
    return estoque.get(produto, 0) < quantidade
