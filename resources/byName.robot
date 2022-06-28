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
    Wait Until Page Contains  Resultados de búsqueda


    TRY
        ${departamentoId}=    Get Departamento Id    ${departamento}
        Click Element  xpath=//*[@id="PROVINCIA"]/option[${departamentoId}]
        Wait Until Page Contains    Pulse sobre el nombre de la Empresa para acceder a la información de la misma
    EXCEPT
        Write No Results
    ELSE
        FOR  ${counter}  IN RANGE  1  ${n}+1  1


            ${page}=    Get Page    ${counter}
            ${indexCompany}=    Get Index Company    ${counter}

            #Click Page
            Click Element    xpath=//*[@id="nacional"]/div[3]/div/div[2]/ul/li[${page}]
            Sleep    2s
            Click Element    xpath=//*[@id="nacional"]/tbody/tr[${indexCompany}]

            ${nombre}    Get Text    xpath=//*[@id="titInner"]/div[1]/ul/li[5]
            ${html_table}=    Get Element Attribute    //*[@id="imprimir"]/table    outerHTML
            Process Table    ${html_table}    ${nombre}    ${companyNameSearch}
            ${ssfilename}    To Lower    ${nombre}
            Capture Page Screenshot    ./screenshots/${ssfilename}.png

            Go Back
        END
    FINALLY
        Close Browser
    END
