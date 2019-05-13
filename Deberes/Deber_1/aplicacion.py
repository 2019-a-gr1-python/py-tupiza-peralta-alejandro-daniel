import tienda_autos

def imprimir_autos():
    try:
        path = './autos.txt'
        archivo_abierto = open(path,mode='r')
        for lineas in archivo_abierto:
            print(lineas)
        archivo.abierto.close
    except:
        print('...')

def buscar_auto():
    print("Buscar auto ")
    placa = input("Ingrese la placa del auto a buscar: ")
    auto = tienda_autos.buscar_por_placa(placa)
    if auto != None:
        imprimir_autos(placa)
        #imprimir_tipos()
        #imprimir_fila(auto)
    else:
        print(f"Auto con placa {placa} no existe")
      
def eliminar_auto(idem):
    lista_autos = []
    inf_eliminada = -1
    try:
        path = './autos.txt'
        archivo_abierto = open(path,mode='r')
        print("Eliminar auto ")
        placa = input("Ingrese la placa del auto a eliminar: ")
        for lineas in archivo_abierto:
            lista_autos.append(lineas)
        archivo_abierto.close()
    except:
        print('Error')
        
    for i in lista_autos:
        y = x.split(';')
        if y[0] == idem:
            inf_eliminada = int(lista_autos.index(x))
            print ('Se elimino el usuario: ' + lista_autos.pop(inf_eliminada))

def actualizar_auto():
    print("Actualizar auto ")
    placa = input("Ingrese la placa del auto a modificar: ")
    auto = tienda_autos.buscar_por_placa(placa)
    def opciones(value):
        try:
            return {
                0: 'placa',
                1: 'color',
                2: 'modelo',
                3: 'precio',
                4: 'hp',
            }[value]
        except KeyError:
            print("Eliga una opcion!")
    if auto != None:
        #imprimir_tipos()
        imprimir_autos(auto)
        print("Opciones")
        print("1.- Modificar color")
        print("2.- Modificar modelo")
        print("3.- Modificar precio")
        print("4.- Modificar hp")
        read = input("Eliga una opcion: ")
        if (read.isnumeric()):
            opc_actualizar = int(read)
        try:
            item_actualizar = opciones(opc_actualizar)
            item = input('Ingrese el nuevo valor: ')
            dato_a_actualizar = {
                llave_a_actualizar: item
            }
            tienda_autos.actualizar_auto(auto, dato_a_actualizar)
        except TypeError:
            print(f'Option {option}')
    else:
        print(f"El auto con placa {placa} no existe")

def opciones_menu(valor):
    try:
        return {
            0: None,
            1: tienda_autos.ingresar_auto,
            2: imprimir_autos,
            3: buscar_auto,
            4: eliminar_auto,
            5: actualizar_auto,
        }[valor]
    except KeyError:
        print("No existe esta opcion")

def aplicacion(option):
    while option != 0:
        print("Menu")
        print("1.- Ingresar auto")
        print("2.- Mostrar lista de autos")
        print("3.- Buscar auto")
        print("4.- Eliminar auto")
        print("5.- Modificar informacion de auto")
        print("0.- Salir")
        read = input("Eliga una opcion: ")
        if (read.isnumeric()):
            option = int(read)
        try:
            opciones_menu(option)()
        except TypeError:
            print(f'Option {option}')

aplicacion(-1)