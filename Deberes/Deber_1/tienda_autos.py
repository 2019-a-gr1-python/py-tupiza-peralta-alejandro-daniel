import archivos_autos

def ingresar_auto():
    print('Ingrese la siguiente informacion del auto')
    modelo = input('Ingrese el modelo: ')
    color = input('Ingrese el color: ')
    placa = input('Ingrese la placa: ')
    precio = input('Ingrese el precio: ')
    hp = input('Ingrese los caballos de fuerza: ')
    auto = modelo + ';' + color + ';' + placa + ';' + precio + ';' + hp
    archivos_autos.agregar_auto('./autos.txt','a',auto)
    
def listar_autos():
    archivo_autos = archivos_autos.leer_archivo_auto('./autos.txt')
    auto = []
    for lista in archivo_autos:
        auto.append(lista)
    return auto

def buscar_por_placa(placa):
    lineas = listar_autos()
    for auto in lineas:
        if auto.get('placa') == placa:
            break
        else:
            auto = None
        return auto
 
def eliminar_auto_por_placa(placa):
    lineas = listar_autos()
    eliminar_auto = buscar_por_placa(placa)
    if eliminar_auto != None:
        lineas.remove(eliminar_auto)
    print(f'Auto eliminado con placa {placa}')
    
def actualizar_auto(auto,actualizar):
    lineas = listar_autos()
    index = lista.index(auto)
    auto.update(actualizar)
    lista[index] = auto
    print(f"Actualizando auto con placa {auto['placa']}")