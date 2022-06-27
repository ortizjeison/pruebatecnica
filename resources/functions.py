import json
from bs4 import BeautifulSoup


departamentos = {
    'AMAZONAS': '2',
    'ANTIOQUIA': '3',
    'ARAUCA': '4',
    'ATLÁNTICO': '5',
    'BOGOTÁ': '6',
    'BOLÍVAR': '7',
    'BOYACÁ': '8',
    'CALDAS': '9',
    'CAQUETÁ': '10',
    'CASANARE': '11',
    'CAUCA': '12',
    'CESAR': '13',
    'CHOCÓ': '14',
    'CÓRDOBA': '15',
    'CUNDINAMARCA': '16',
    'GUAINÍA': '17',
    'GUAVIARE': '18',
    'HUILA': '19',
    'LA GUAJIRA': '20',
    'MAGDALENA': '21',
    'META': '22',
    'NARIÑO': '23',
    'NORTE SANTANDER': '24',
    'PUTUMAYO': '25',
    'QUINDÍO': '26',
    'RISARALDA': '27',
    'SAN ANDRÉS': '28',
    'SANTANDER': '29',
    'SUCRE': '30',
    'TOLIMA': '31',
    'VALLE': '32',
    'VAUPÉS': '33',
    'VICHADA': '34',
    'No Aplica': '35'
}

def get_number_results(string):
    number = string[string.find("(")+1:string.find(")")]
    return number

def get_departamentos():
    return departamentos

def get_departamento_id(nombre):

    if(departamentos.get(nombre)!='None'):
        return departamentos.get(nombre)
    else:
        return False

def process_table(html,nombre):

    table_data = [[cell.text for cell in row("td")]
                  for row in BeautifulSoup(html)("tr")]

    result = {"Key":[], "Value":[]}

    dict = '{}'
    company = json.loads(dict)

    company.update(
        {"nombre":nombre.replace("/ ","")}
    )

    for element in table_data:
        if(len(element)>1):
            result["Key"].append(element[0].replace(":",""))
            result["Value"].append(element[1])
            temp={element[0].replace(":",""):element[1]}
            company.update(temp)

    with open(r'C:\Users\jeiso\Documents\GitHub\pruebatecnica\results\company.json', 'w', encoding='utf-8') as outfile:
        json.dump(company, outfile, ensure_ascii=False)
    return 0



#yfile = open(r"C:\Users\jeiso\Documents\GitHub\pruebatecnica\results\table.txt", encoding='utf-8')
#process_table(myfile,'Empresa123')