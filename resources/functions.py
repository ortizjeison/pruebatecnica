import json

def get_number_results(string, vaina):
    number = string[string.find("(")+1:string.find(")")]
    return number+vaina

def get_departamento_id(nombre):

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

    if(departamentos.get(nombre)!='None'):
        return departamentos.get(nombre)
    else:
        return False


def send_company_info(ICI,NIT,razonSocial,formaJuridica,departamento,direccion,tel,email,actividadCIIU,fechaConstitucion,matricula,balance,fechaUltimoDato,fechaActualizacionCamara):
    companyInfo = {
    "ICI":ICI,
    "Nit":NIT,
    "Razón Social":razonSocial,
    "Forma Jurídica":formaJuridica,
    "Departamento":departamento,
    "Dirección Actual":direccion,
    "Teléfono":tel,
    "Email":email,
    "Actividad CIIU":actividadCIIU,
    "Fecha Constitución":fechaConstitucion,
    "Matrícula Mercantil":matricula,
    "Último Balance disponible en eInforma":balance,
    "Fecha Último Dato":fechaUltimoDato,
    "Fecha Actualización Cámara Comercio":fechaActualizacionCamara
    }

    with open('./temp.json', 'w', encoding='utf-8') as outfile:
        json.dump(companyInfo, outfile, ensure_ascii=False)
    return 0