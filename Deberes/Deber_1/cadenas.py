def convertir_cadena(linea):
    cadena = (linea + '').replace('\n','').split(';')
    datos = {
        'placa' : parte_linea[0],
        'color'   : parte_linea[1],
        'modelo'   : parte_linea[2],
        'precio'   : parte_linea[3],
        'hp'   : parte_linea[4],
    }
    return datos

def convertir_diccionario(auto):
    return f"{auto['placa']};{auto['color']};{auto['modelo']};{auto['precio']};{auto['hp']}"