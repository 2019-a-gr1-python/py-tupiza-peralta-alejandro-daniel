def convertir_cadena(linea):
    cadena = (linea + '').replace('\n','').split(';')
    datos = {
        'placa' : cadena[0],
        'color'   : cadena[1],
        'modelo'   : cadena[2],
        'precio'   : cadena[3],
        'hp'   : cadena[4],
    }
    return datos

def convertir_diccionario(auto):
    return f"{auto['placa']};{auto['color']};{auto['modelo']};{auto['precio']};{auto['hp']}"