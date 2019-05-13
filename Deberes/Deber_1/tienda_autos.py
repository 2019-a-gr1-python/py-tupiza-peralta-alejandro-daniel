import cadenas

def agregar_auto(path,option,*autos):
    try:
        archivo_escritura_auto = open(path,option)
        for linea in autos:
            archivo_escritura_auto.write(linea + '\n')
        archivo_escritura_auto.close()
        print('Informacion guardada')
    except:
        print('La informacion no se ha guardado')  
        
def ingresar_auto():
    print('Ingrese la siguiente informacion del auto')
    placa = input('Ingrese la placa: ')
    color = input('Ingrese el color: ')
    modelo = input('Ingrese el modelo: ')
    precio = input('Ingrese el precio: ')
    hp = input('Ingrese los caballos de fuerza: ')
    auto = placa + ';' + color + ';' + modelo + ';' + precio + ';' + hp + '\n'
    archivo_auto = agregar_auto('./autos.txt','a',auto)

def listar_autos():
    archivo_auto = leer_archivo_auto('./autos.txt')
    auto = []
    for lista in archivo_auto:
        auto.append(cadenas.convertir_cadena(lista))
    return auto

def buscar_por_placa(placa):
    lineas = listar_autos()
    for auto in lineas:
        if auto.get('placa') == placa:
            break
        else:
            auto = None
   ´ return auto   
    
def leer_archivo_auto(path):
    try:
        lineas = []
        archivo = open(path,mode='r')
        arreglo_lineas_archivo = archivo.readlines()
        for linea in arreglo_lineas_archivo:
            lineas.append(linea)
        archivo.close()
        return lineas
    except Exception:
        print("No se puede leer el archivo: " + path)    

def actualizar_auto(auto,actualizar):
    lineas = listar_autos()
    index = lista.index(auto)
    auto.update(actualizar)
    lista[index] = auto
    print(f"Actualizando auto con placa {auto['placa']}")