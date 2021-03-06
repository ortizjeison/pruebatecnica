import json
from bs4 import BeautifulSoup
from re import sub
import math
from pysondb import db
import unidecode
from difflib import SequenceMatcher


pageSize = 12
maxResults = 30
path = r'results\temp.json'


departamentos = {
    'Filtrar departamento': '1',
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
    print("NUMBER OF RESLTS: "+str(number))
    return number

def get_departamentos():
    return departamentos

def get_departamento_id(nombre):

    if(departamentos.get(nombre)!= None):
        return departamentos.get(nombre)
    else:
        return str(1)

def process_table(html,nombre,companyNameSearch):


    #path = r'..\api\results\temp.json'

    database = db.getDb(path)

    table_data = [[cell.text for cell in row("td")]
                  for row in BeautifulSoup(html)("tr")]

    result = {"Key":[], "Value":[]}

    dict = '''{
    "score":"Null",
    "ici":"Null",
    "nit":"Null",
    "razonSocial":"Null",
    "formaJuridica":"Null",
    "departamento":"Null",
    "direccionActual":"Null",
    "telefono":"Null",
    "email":"Null",
    "actividadCiiu":"Null",
    "fechaConstitucion":"Null",
    "matriculaMercantil":"Null",
    "fechaUltimoDato":"Null",
    "fechaActualizacionCamaraComercio":"Null",
    "ultimoBalanceDisponibleEnEinforma":"Null"
    }'''

    company = json.loads(dict)
    nombre = nombre.replace("/ ","")

    company.update(
        {"score": str(SequenceMatcher(None, nombre, companyNameSearch).ratio())}
    )

    company.update(
        {"nombre": nombre}
    )


    company.update(
        {"screenshotURL":r'results\screenshots\{}.png'.format(to_lower(nombre.replace("/ ","")))}
    )

    for element in table_data:
        if(len(element)>1):

            key = camel_case(element[0]).replace(":","")

            temp={key:element[1]}
            company.update(temp)


    id = database.add(company)



def to_lower(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return unidecode.unidecode(s[:].lower())

def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  temp = ''.join([s[0].lower(), s[1:]])
  return unidecode.unidecode(temp)

def get_page(n):
    value = n/pageSize
    maxPages = math.ceil(maxResults/pageSize)


    for i in range (1,maxPages+1):
        if(i-1<=value<=i):
            return i+1

def get_index_company(n):
    return n - (pageSize*(get_page(n)-2))

def write_no_results():
    with open(path, "w", encoding='utf-8') as jsonfile:
        json.dump({"data":"No ha sido posible encontrar ningún resultado relacionado con su búsqueda. Por favor, revise los términos de búsqueda e inténtelo de nuevo."}, jsonfile, ensure_ascii=False)

#num = 20
#print("For num "+str(num)+": page:"+str(get_page(num))+" / index:"+str(get_index_company(num)))

#myfile = open(r"C:\Users\jeiso\Documents\GitHub\pruebatecnica\results\table.txt", encoding='utf-8')
#process_table(myfile,'Empresa5213')
