'''
utils.py: Modulo para definir los metodos de funcionalidad auxiliar
'''
from flask import jsonify
from cerberus import Validator


def json_message(msg, code=200):
    '''
    Metodo que devuelve un mensaje en formato json
    '''
    return jsonify({
        "message": msg,
        'statusCode': code
    })

def validate_parameters(parameters, schema):
    v = Validator(schema)
    v.allow_unknown = True
    if not v.validate(parameters):
        return jsonify({
            "errors": v.errors
        })