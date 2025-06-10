*** Settings ***
Resource    resources/keywords.robot

*** Test Cases ***
Visualizar Estoque Com Produtos
    Iniciar Sessão

    ${resp}=    GET On Session    api    /estoque/
    Should Be Equal As Integers    ${resp.status_code}    200
    ${produtos}=    Set Variable    ${resp.json()}
    Length Should Be Greater Than    ${produtos}    0
