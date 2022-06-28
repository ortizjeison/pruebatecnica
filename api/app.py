from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
import robot
import os


app = APIFlask(__name__)

class QuerySchema(Schema):
    nombre = String()
    nit = Integer(required=True)
    n = Integer(required=True)


@app.get('/query/<int:param>')
#@app.output(PetOutSchema)
def query(param):
    os.system("robot -d ./results -v companyNameSearch:ol -v n:2 -v departamento:BOGOTÁ ../resources/first.robot")

    return "hola amigos"+str(param)