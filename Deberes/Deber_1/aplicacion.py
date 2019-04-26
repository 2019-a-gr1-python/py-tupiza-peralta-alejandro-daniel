import tienda_autos

def imprimir_tipos():
    print('%-10s%-10s%-15s%-20s%-10s' % ('Placa', 'Color', 'Modelo', 'Precio', 'Caballos de fuerza'))


def imprimir_fila(auto):
    print('%(placa)-10%(color)-10%(modelo)-15%(precio)-20%(hp)-10s' % auto)

def imprimir_autos():
    print("Tienda de Autos ")
    #lista = tienda_autos.listar_autos()
    lista = tienda_autos.leer_archivo_auto()
    imprimir_tipos()
    for auto in lista:
        imprimir_fila(auto)
        
def buscar_auto():
    print("Buscar auto ")
    placa = input("Ingrese la placa del auto a buscar: ")
    auto = tienda_autos.buscar_por_placa(placa)
    if auto != None:
        imprimir_tipos()
        imprimir_fila(auto)
    else:
        print(f"Auto con placa {placa} no existe")
      
def eliminar_auto():
    print("Eliminar auto ")
    placa = input("Ingrese la placa del auto a eliminar: ")
    tienda_autos.eliminar_auto_por_placa(placa)
    
    
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
    if zapato != None:
        imprimir_tipos()
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

def opciones_menu(value):
    try:
        return {
            0: None,
            1: tienda_autos.ingresar_auto,
            2: imprimir_autos,
            #2: tienda_autos.leer_archivo_auto,
            3: buscar_auto,
            4: eliminar_auto,
            5: actualizar_auto,
        }[value]
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