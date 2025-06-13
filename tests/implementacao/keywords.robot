*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://localhost:8000

*** Keywords ***
Iniciar Sessão
    Create Session    api    ${BASE_URL}

Criar Produto
    [Arguments]    ${nome}    ${tipo}    ${marca}    ${modelo}    ${preco}    ${quantidade}
    ${body}=    Create Dictionary
    ...    nome=${nome}
    ...    tipo=${tipo}
    ...    marca=${marca}
    ...    modelo=${modelo}
    ...    preco=${preco}
    ...    quantidade_estoque=${quantidade}
    ${resp}=    POST On Session    api    /produtos/    json=${body}
    Should Be Equal As Integers    ${resp.status_code}    200
    RETURN    ${resp.json()}