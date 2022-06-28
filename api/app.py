from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask import request
from marshmallow import Schema, fields, post_load, validates, validate, ValidationError

import robot
import os
import json

departamentos = ['AMAZONAS','ANTIOQUIA','ARAUCA','ATLÁNTICO','BOGOTÁ','BOLÍVAR','BOYACÁ','CALDAS','CAQUETÁ','CASANARE','CAUCA','CESAR','CHOCÓ','CÓRDOBA','CUNDINAMARCA','GUAINÍA','GUAVIARE','HUILA','LA GUAJIRA','MAGDALENA','META','NARIÑO','NORTE SANTANDER','PUTUMAYO','QUINDÍO','RISARALDA','SAN ANDRÉS','SANTANDER','SUCRE','TOLIMA','VALLE','VAUPÉS','VICHADA','No Aplica']

app = APIFlask(__name__)

class QuerySchema(Schema):
    nombre = String()
    nit = Integer()
    n = Integer(required=True)
    departamento = String(required=True, validate=OneOf(departamentos))

#/<string:nombre>/<string:departamento>/<int:n>

@app.get('/queryByName')

def query():
    argName = request.args.get("name")

    #os.system("robot -d ./results -v companyNameSearch:ol -v n:2 -v departamento:BOGOTÁ ../resources/first.robot")
    print(nameArg)

    with open('results/temp.json', encoding='utf-8') as jsonFile:
        data = json.load(jsonFile)

    return data