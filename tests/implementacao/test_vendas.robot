*** Settings ***
Library     Collections
Resource    keywords.robot

*** Test Cases ***
Vender Produto Existente
    Iniciar Sessão

    ${placa_mae}=    Criar Produto    ASUS B550M    placa-mãe    ASUS    B550M    800.00    5

    ${body}=    Create Dictionary
    ...    produto_id=${placa_mae["id"]}
    ...    quantidade=2
    ...    tipo_venda=direta

    ${resp}=    POST On Session    api    /vendas/    json=${body}
    Should Be Equal As Integers    ${resp.status_code}    200
    Dictionary Should Contain Key    ${resp.json()}    mensagem
