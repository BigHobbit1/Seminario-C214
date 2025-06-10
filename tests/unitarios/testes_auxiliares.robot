*** Settings ***
Library    OperatingSystem
Library    BuiltIn
Library    lib_robot.py

*** Test Cases ***

# ======== Casos Positivos ========
Validar Nome Correto
    ${resultado}=    Validar Nome    Produto X
    Should Be True    ${resultado}

Validar Preço Correto
    ${preco}=    Evaluate    100.5
    ${resultado}=    validar_preco    ${preco}
    Should Be True    ${resultado}

Validar Quantidade Correta
    ${quantidade}=    Evaluate    10
    ${resultado}=    validar_quantidade    ${quantidade}
    Should Be True    ${resultado}

Criar Produto Válido
    ${preco}=        Evaluate    200.0
    ${quantidade}=   Evaluate    10
    ${resultado}=    criar_produto_valido    Produto X    Tipo A    Marca Y    Modelo 1    ${preco}    ${quantidade}
    Should Be True    ${resultado}

Calcular Total Estoque
    ${p1}=    Evaluate    {"quantidade_estoque": 5}
    ${p2}=    Evaluate    {"quantidade_estoque": 10}
    ${produtos}=    Create List    ${p1}    ${p2}
    ${resultado}=    calcular_total_estoque    ${produtos}
    Should Be Equal As Integers    ${resultado}    15

Verificar Peças Necessárias Presentes
    ${resultado}=    Verificar Pecas Necessarias    ["CPU", "RAM", "HD"]    ["CPU", "HD"]
    Should Be True    ${resultado}

Montar Computador com Estoque
    ${estoque}=    Evaluate    {"CPU": 1, "RAM": 1}    modules=builtins
    ${resultado}=    montar_computador    ${estoque}    ["CPU", "RAM"]
    Should Be True    ${resultado}

Pode Realizar Venda
    ${estoque}=    Create Dictionary    Mouse=5
    ${resultado}=    Pode Realizar Venda    ${estoque}    Mouse    3
    Should Be True    ${resultado}

Registrar Venda Válida
    ${estoque}=    Evaluate    {"Teclado": 10}    modules=builtins
    ${quantidade}=    Evaluate    3    modules=builtins
    ${resultado}=    registrar_venda    ${estoque}    Teclado    ${quantidade}
    Dictionary Should Contain Value    ${resultado}    7

Verificar Peças Necessárias Ausentes (Negativo Esperado)
    ${resultado}=    Verificar Pecas Necessarias    ["CPU", "RAM"]    ["CPU", "GPU"]
    Should Be True    not ${resultado}

# ======== Casos Negativos ========
Nome Inválido Vazio
    ${resultado}=    Nome Invalido    ${EMPTY}
    Should Be True    ${resultado}

Nome Inválido Tipo Errado
    ${valor}=    Evaluate    123
    ${resultado}=    nome_invalido    ${valor}
    Should Be True    ${resultado}

Preço Inválido Negativo
    ${resultado}=    Preco Invalido    -10.5
    Should Be True    ${resultado}

Preço Inválido Tipo Errado
    ${resultado}=    Preco Invalido    abc
    Should Be True    ${resultado}

Quantidade Inválida Negativa
    ${resultado}=    Quantidade Invalida    -1
    Should Be True    ${resultado}

Quantidade Inválida Tipo Errado
    ${resultado}=    Quantidade Invalida    Dois
    Should Be True    ${resultado}

Montar Computador com Peças Faltando
    ${estoque}=    Create Dictionary    CPU=1    RAM=0
    ${resultado}=    Montar Computador Faltando Pecas    ${estoque}    ["CPU", "RAM"]
    Should Be True    ${resultado}

Tentar Venda com Estoque Insuficiente
    ${estoque}=    Create Dictionary    Monitor=2
    ${resultado}=    Tentar Venda Sem Estoque    ${estoque}    Monitor    5
    Should Be True    ${resultado}

Registrar Venda Inválida (Sem Estoque)
    ${estoque}=    Create Dictionary    SSD=1
    Run Keyword And Expect Error    *Estoque insuficiente para a venda.*    registrar_venda    ${estoque}    SSD    5