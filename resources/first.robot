****** Settings ***

Documentation  holamundo

Library  SeleniumLibrary
Library  functions.py

*** Variables ***

${BROWSER}  Chrome
${URL}  https://www.einforma.co/buscador-empresas-empresarios
${companyNameSearch}
${companyNITSearch}
${departamento}
${numberOfResults}
${n}

*** Test Cases ***
This is my test case
    [Documentation]  hello world

    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Wait Until Page Contains  Buscar y verificar empresas por nombre
    Input Text  search  ${companyNameSearch}
    Click Button  xpath=//*[@id="buscador_cabecera"]/input[2]
    Wait Until Page Contains  Resultados de búsqueda

    #Seleccionar departamento
    ${departamentoId}=    Get Departamento Id    ${departamento}
    Click Element  xpath=//*[@id="PROVINCIA"]/option[${departamentoId}]

    ${resultsText}  Get Text  xpath://*[@id="a_nacional"]
    ${numberResults}=  Get Number Results  ${resultsText}
    #Log To Console    Hola====${numberResults}

    #if Get Number Results > 0
    #Ciclo para recorrer cada empresa
    Wait Until Page Contains    Denominación
    Click Element    xpath=//*[@id="nacional"]/tbody/tr[1]


    ${nombre}    Get Text    xpath=//*[@id="titInner"]/div[1]/ul/li[5]
    ${html_table}=    Get Element Attribute    //*[@id="imprimir"]/table    outerHTML
    Process Table    ${html_table}    ${nombre}

    Capture Page Screenshot    ${n}.png

    Sleep    5s
    Close Browser