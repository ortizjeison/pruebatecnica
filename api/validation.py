from marshmallow import Schema, fields, post_load, validates, validate, ValidationError



class Query:
    def __init__(self,nombre,departamento,nit,n):
        self.nombre = nombre
        self.departamento = departamento
        self.nit = nit
        self.n = n
        


class QuerySchema(Schema):
    nombre = fields.String()
    nit = fields.Int(validate=validate.Range(min=0000000000, max=9999999999))
    n = fields.Integer(
        required=True,
        error_messages={"required": {"message": "n es un campo obligatorio", "code": 400}}
    )

    @validates("n")
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("N debe ser mayor que 0.")
        if value > 30:
            raise ValidationError("N debe ser menor o igual a 30.")



schema = QuerySchema()

inputData = {"nombre": "Olimpica", "nit": "123456789111", "n": 6}

try:
    print(schema.load(inputData))
except ValidationError as err:
    print(err.messages)