****** Settings ***

Documentation  holamundo

Library  SeleniumLibrary

*** Variables ***

${BROWSER}  Chrome
${URL}  https://www.einforma.co/buscador-empresas-empresarios
${companyId}
${n}

*** Test Cases ***
This is my test case
    [Documentation]  hello world
    [tags]  Smoke
    Open Browser    ${URL}  ${Browser}
    Maximize Browser Window
    Wait Until Page Contains    Buscar y verificar empresas por nombre
    Input Text  search    ${companyId}
    Click Button    xpath=//*[@id="buscador_cabecera"]/input[2]
    Wait Until Page Contains    Resultados de búsqueda
    Capture Page Screenshot    holamundo.png
    Close Browser
