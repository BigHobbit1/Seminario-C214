from pathlib import Path

testes_robot = """
*** Settings ***
Library           Collections
Library           OperatingSystem
Library           BuiltIn
Library           ../../app/auxiliar.py


*** Test Cases ***

# ======== Casos Positivos ========
Validar Nome Correto
    ${resultado}=    Call Method    auxiliar    validar_nome    Produto X
    Should Be True    ${resultado}

Validar Preço Correto
    ${resultado}=    Call Method    auxiliar    validar_preco    100.50
    Should Be True    ${resultado}

Validar Quantidade Correta
    ${resultado}=    Call Method    auxiliar    validar_quantidade    5
    Should Be True    ${resultado}

Criar Produto Válido
    ${resultado}=    Call Method    auxiliar    criar_produto_valido    Produto X    Tipo A    Marca Y    Modelo 1    200.0    10
    Should Be True    ${resultado}

Calcular Total Estoque
    ${produtos}=    Create List    {"quantidade_estoque": 5}    {"quantidade_estoque": 10}
    ${resultado}=    Call Method    auxiliar    calcular_total_estoque    ${produtos}
    Should Be Equal As Integers    ${resultado}    15

Verificar Peças Necessárias Presentes
    ${resultado}=    Call Method    auxiliar    verificar_pecas_necessarias    ["CPU", "RAM", "HD"]    ["CPU", "HD"]
    Should Be True    ${resultado}

Montar Computador com Estoque
    ${estoque}=    Create Dictionary    CPU=1    RAM=1
    ${resultado}=    Call Method    auxiliar    montar_computador    ${estoque}    ["CPU", "RAM"]
    Should Be True    ${resultado}

Pode Realizar Venda
    ${estoque}=    Create Dictionary    Mouse=5
    ${resultado}=    Call Method    auxiliar    pode_realizar_venda    ${estoque}    Mouse    3
    Should Be True    ${resultado}

Registrar Venda Válida
    ${estoque}=    Create Dictionary    Teclado=10
    ${novo_estoque}=    Call Method    auxiliar    registrar_venda    ${estoque}    Teclado    3
    Dictionary Should Contain Value    ${novo_estoque}    7

# ======== Casos Negativos ========
Nome Inválido Vazio
    ${resultado}=    Call Method    auxiliar    nome_invalido    ${EMPTY}
    Should Be True    ${resultado}

Nome Inválido Tipo Errado
    ${resultado}=    Call Method    auxiliar    nome_invalido    123
    Should Be True    ${resultado}

Preço Inválido Negativo
    ${resultado}=    Call Method    auxiliar    preco_invalido    -10.5
    Should Be True    ${resultado}

Preço Inválido Tipo Errado
    ${resultado}=    Call Method    auxiliar    preco_invalido    abc
    Should Be True    ${resultado}

Quantidade Inválida Negativa
    ${resultado}=    Call Method    auxiliar    quantidade_invalida    -1
    Should Be True    ${resultado}

Quantidade Inválida Tipo Errado
    ${resultado}=    Call Method    auxiliar    quantidade_invalida    Dois
    Should Be True    ${resultado}

Montar Computador com Peças Faltando
    ${estoque}=    Create Dictionary    CPU=1    RAM=0
    ${resultado}=    Call Method    auxiliar    montar_computador_faltando_pecas    ${estoque}    ["CPU", "RAM"]
    Should Be True    ${resultado}

Tentar Venda com Estoque Insuficiente
    ${estoque}=    Create Dictionary    Monitor=2
    ${resultado}=    Call Method    auxiliar    tentar_venda_sem_estoque    ${estoque}    Monitor    5
    Should Be True    ${resultado}

Registrar Venda Inválida (Sem Estoque)
    ${estoque}=    Create Dictionary    SSD=1
    Run Keyword And Expect Error    *    Call Method    auxiliar    registrar_venda    ${estoque}    SSD    2

Verificar Peças Necessárias Ausentes
    ${resultado}=    Call Method    auxiliar    verificar_pecas_necessarias    ["CPU", "RAM"]    ["CPU", "GPU"]
    Should Be False    ${resultado}
"""

testes_path = Path("testes/unitarios/testes_auxiliares.robot")
testes_path.parent.mkdir(parents=True, exist_ok=True)
testes_path.write_text(testes_robot.strip(), encoding="utf-8")

testes_path
