*** Settings ***
Library           api_mock_library.py
Library           Collections
Library           BuiltIn

*** Test Cases ***

Mock - Listar Produtos em Estoque
    ${produtos}=    Get Produtos Mock
    ${length}=    Get Length    ${produtos}
    Should Be True    ${length} > 0
    Dictionary Should Contain Key    ${produtos[0]}    nome
    Dictionary Should Contain Key    ${produtos[0]}    tipo
    Dictionary Should Contain Key    ${produtos[0]}    quantidade_estoque

Mock - Venda Bem-Sucedida
    ${quantidade}=    Convert To Integer    3
    ${resposta}=    Realizar Venda Mock    Ryzen 7    ${quantidade}
    Should Be Equal As Integers    ${resposta["status"]}    200
    Should Be Equal    ${resposta["mensagem"]}    Venda realizada com sucesso

Mock - Venda com Falha por Estoque
    ${quantidade}=    Convert To Integer    10
    ${resposta}=    Realizar Venda Mock    Ryzen 7    ${quantidade}
    Should Be Equal As Integers    ${resposta["status"]}    400
    Should Contain    ${resposta["mensagem"]}    insuficiente


Mock - Visualizar Estoque Com Produtos
    ${produtos}=    Get Produtos Mock
    ${length}=    Get Length    ${produtos}
    Should Be True    ${length} > 0
    Dictionary Should Contain Key    ${produtos[0]}    nome
    Dictionary Should Contain Key    ${produtos[0]}    tipo
    Dictionary Should Contain Key    ${produtos[0]}    preco
    Dictionary Should Contain Key    ${produtos[0]}    quantidade_estoque

Mock - Montar Computador Com Peças No Estoque
    ${resposta}=    Montar Computador Mock    Gamer Top    RTX 4060    Ryzen 5 5600G
    Should Be Equal As Integers    ${resposta["status"]}    200
    Should Be Equal    ${resposta["mensagem"]}    Computador montado com sucesso
    Dictionary Should Contain Key    ${resposta}    id
    Dictionary Should Contain Key    ${resposta}    nome

Mock - Verificar Detalhes do Produto
    ${produto}=    Get Detalhes Produto Mock    RTX 4060
    Should Be Equal As Numbers    ${produto["preco"]}    2500.00
    Should Be Equal    ${produto["nome"]}    RTX 4060
    Should Be Equal    ${produto["tipo"]}    placa de vídeo
    Should Be Equal As Integers    ${produto["quantidade_estoque"]}    2

Mock - Buscar Histórico de Vendas
    ${historico}=    Get Historico Vendas Mock
    ${length}=    Get Length    ${historico}
    Should Be True    ${length} > 0
    Dictionary Should Contain Key    ${historico[0]}    id_venda
    Dictionary Should Contain Key    ${historico[0]}    produto
    Dictionary Should Contain Key    ${historico[0]}    data_venda
    Dictionary Should Contain Key    ${historico[0]}    quantidade

Mock - Atualizar Quantidade no Estoque
    ${resposta}=    Atualizar Quantidade Estoque Mock    Ryzen 7    5
    Should Be Equal As Integers    ${resposta["status"]}    200
    Should Be Equal    ${resposta["mensagem"]}    Quantidade de produto atualizada com sucesso
