import json

def convertir_cadena(linea):
    cadena = (linea + '').replace('\n','').split(';')
    datos = {
        'placa' : 'Juan Perez',
        'color'   : 18,
        'modelo'   : 'Panama'
        'precio'   : 'Panama'
        'hp'   : 'Panama'
    }
    json_str = json.dumps(datos)

    print('Datos en formato JSON:', json_str)