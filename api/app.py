from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
from flask import request
from marshmallow import Schema, fields, post_load, validates, validate, ValidationError
import os
import json

departamentos = ['AMAZONAS','ANTIOQUIA','ARAUCA','ATLÁNTICO','BOGOTÁ','BOLÍVAR','BOYACÁ','CALDAS','CAQUETÁ','CASANARE','CAUCA','CESAR','CHOCÓ','CÓRDOBA','CUNDINAMARCA','GUAINÍA','GUAVIARE','HUILA','LA GUAJIRA','MAGDALENA','META','NARIÑO','NORTE SANTANDER','PUTUMAYO','QUINDÍO','RISARALDA','SAN ANDRÉS','SANTANDER','SUCRE','TOLIMA','VALLE','VAUPÉS','VICHADA','No Aplica']

jsonFilePath = 'results/temp.json'

app = APIFlask(__name__)

class QueryByNameSchema(Schema):
    nombre = fields.String(required=True)
    departamento = fields.String(required=True,validate=validate.OneOf(departamentos))

    #nit = fields.Int(validate=validate.Range(min=0000000000, max=9999999999))

    n = fields.Integer(
        required=True,
        error_messages={"required": {"message": "n es un campo obligatorio", "code": 400}}
    )

    @validates("n")
    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError("N debe ser un entero mayor que 0.")
        if value > 30:
            raise ValidationError("N debe ser un entero menor o igual a 30.")

@app.get('/queryByName')
def queryByName():

    try:
        os.remove(jsonFilePath)
    except:
        pass

    argNombre = request.args.get("name")
    argDepartamento = request.args.get("departamento")
    argN = request.args.get("n")

    schema = QueryByNameSchema()
    inputData = {"nombre": argNombre,"departamento": argDepartamento,"n": argN}

    try:
        
        schema.load(inputData)
        robotRun = f"robot -d ./results -v companyNameSearch:{argNombre} -v n:{argN} -v departamento:{argDepartamento} ../resources/first.robot"

        os.system(robotRun)

        with open(jsonFilePath, encoding='utf-8') as jsonFile:
            data = json.load(jsonFile)

        os.remove(jsonFilePath)

        return data

        
    except ValidationError as err:
        return err.messages