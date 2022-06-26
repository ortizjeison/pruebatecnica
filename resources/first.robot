****** Settings ***

Documentation  holamundo

Library  SeleniumLibrary
Library  functions.py

*** Variables ***

${BROWSER}  Chrome
${URL}  https://www.einforma.co/buscador-empresas-empresarios
<<<<<<< HEAD
${companyId}    olimpica
${departamento}
${numberOfResults}
=======
${companyId}
>>>>>>> parent of 0c1bd30 (new tests)
${n}

*** Test Cases ***
This is my test case
    [Documentation]  hello world

    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
<<<<<<< HEAD
    Wait Until Page Contains  Buscar y verificar empresas por nombre
    Input Text  search  ${companyId}
    Click Button  xpath=//*[@id="buscador_cabecera"]/input[2]
    Wait Until Page Contains  Resultados de búsqueda

    #Seleccionar departamento
    ${departamentoId}=    Get Departamento Id    ${departamento}
    Click Element  xpath=//*[@id="PROVINCIA"]/option[${departamentoId}]

    ${data}  Get Text    xpath://*[@id="content"]/div/div[1]
    ${numberResult}  Get Text  xpath://*[@id="a_nacional"]

    #if Get Number Results > 0
    #Ciclo para recorrer cada empresa
    Wait Until Page Contains    Denominación
    Click Element    xpath=//*[@id="nacional"]/tbody/tr[1]
    #Basica
    ${ICI}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[2]/td[2]
    ${NIT}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[3]/td[2]
    ${razonSocial}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[4]/td[2]
    ${formaJuridica}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[5]/td[2]
    ${departamento}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[6]/td[2]
    ${direccion}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[7]/td[2]
    ${tel}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[8]/td[2]
    ${email}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[9]/td[2]
    ${actividadCIIU}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[10]/td[2]
    ${fechaConstitucion}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[11]/td[2]
    ${matricula}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[12]/td[2]
    #Actualizacion
    ${balance}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[14]/td[2]
    ${fechaUltimoDato}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[15]/td[2]
    ${fechaActualizacionCamara}   Get Text    xpath=//*[@id="imprimir"]/table/tbody/tr[16]/td[2]

    ${sendData}=  Send Company Info  ${ICI}    ${NIT}    ${razonSocial}    ${formaJuridica}    ${departamento}    ${direccion}    ${tel}    ${email}    ${actividadCIIU}    ${fechaConstitucion}    ${matricula}    ${balance}    ${fechaUltimoDato}    ${fechaActualizacionCamara}

    #Close Browser
=======
    Wait Until Page Contains    Buscar y verificar empresas por nombre
    Input Text  search    ${companyId}
    Click Button    xpath=//*[@id="buscador_cabecera"]/input[2]
    Wait Until Page Contains    Resultados de búsqueda
    Capture Page Screenshot    holamundo.png
    Close Browser
>>>>>>> parent of 0c1bd30 (new tests)
