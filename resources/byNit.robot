****** Settings ***

Documentation  holamundo

Library  SeleniumLibrary
Library  functions.py

*** Variables ***

${BROWSER}  Edge
${URL}  https://www.einforma.co/buscador-empresas-empresarios
${companyNameSearch}
${departamento}
${n}

*** Test Cases ***
This is my test case
    [Documentation]  hello world

    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Wait Until Page Contains  Buscar y verificar empresas por nombre
    Input Text  search  ${companyNameSearch}
    Click Button  xpath=//*[@id="buscador_cabecera"]/input[2]

    #Seleccionar departamento
    ${departamentoId}=    Get Departamento Id    ${departamento}
    #Click Element  xpath=//*[@id="PROVINCIA"]/option[${departamentoId}]

    TRY
        Wait Until Page Contains    Información Básica
    EXCEPT
        Write No Results
    ELSE
        ${nombre}    Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[3]/td[2]/a
        ${html_table}=    Get Element Attribute    //*[@id="imprimir"]/table    outerHTML
        Process Table    ${html_table}    ${nombre}    ${companyNameSearch}
        ${ssfilename}    To Lower    ${nombre}
        Capture Page Screenshot    ./screenshots/${ssfilename}.png

        Go Back

    FINALLY
        Close Browser
    END
