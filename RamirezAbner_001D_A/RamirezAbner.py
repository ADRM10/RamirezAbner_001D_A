from os import system
system("cls")

#General
juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False,
'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True,
'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True,
'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False,
'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False,
'IronGate']
}

inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}

#--------------------------
#Funciones generales
def leer_opcion() -> None:
    try: 
        
        opcion = int(input("Ingrese una de las opciones: "))
        if opcion >=1 and opcion <=6:
            return opcion
        else:
            return 0
    
    except ValueError:
        print("Error. Solo se permiten valores enteros.")
        return 0

def buscar_codigo(codigo_buscado: str, inventario: dict) -> bool:
    for codigo in inventario:
        if codigo_buscado == codigo:
            return True
    else:
        return False
    
#--------------------------
#Funcion opcion 1
def stock_plataforma(plataforma_buscada: str, juegos: dict, inventario: dict) -> None:
    total = 0
    for codigo in juegos:
        plataforma = juegos[codigo][1]
        stock = inventario[codigo][1]
        
        if plataforma_buscada == plataforma:
            total+=stock
    print(f"Stock total en la plataforma ({plataforma_buscada}) es de: {total}")
    
#--------------------------
#Funcion opcion 2
def busqueda_precio(p_min: int, p_max: int, juegos: dict, inventario: dict) -> None:
    lista_juegos = []
    for codigo in inventario:
        titulo = juegos[codigo][0]
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        
        if precio >= p_min and precio <= p_max and stock !=0:
            juego = titulo+"--"+codigo
            lista_juegos.append(juego)
    
    if len(lista_juegos) == 0:
        print("No hay juegos en ese rango de precios.")
    
    lista_juegos.sort()
    for juego in lista_juegos:
        print(juego)
        
#--------------------------
#Funcion opcion 3
def actualizar_precio(codigo: str, nuevo_precio: int, inventario: dict) -> bool:
    existe = buscar_codigo(codigo, inventario)
    if existe:
        inventario[codigo][0]=nuevo_precio
        return True
    else:
        return False
    
#--------------------------
#Funcion opcion 4
def validar_codigo(codigo: str) -> bool:
    if codigo == "":
        return False
    else:
        return True

def validar_titulo(titulo: str) -> bool:
    if titulo == "":
        return False
    else:
        return True

def validar_plataforma(plataforma: str) -> bool:
    if plataforma == "":
        return False
    else:
        return True

def validar_genero(genero: str) -> bool:
    if genero == "":
        return False
    else:
        return True

def validar_clasificacion(clasificacion: str) -> bool:
    if clasificacion == "E" or clasificacion == "T" or clasificacion == "M":
        return True
    else:
        return False

def validar_multiplayer(multiplayer: str) -> bool:
    if multiplayer == "s" or multiplayer == "n":
        return True
    else:
        return False

def validar_editor(editor: str) -> bool:
    if editor == "":
        return False
    else:
        return True

def validar_precio(precio: int) -> bool:
    if precio >0:
        return True
    else:
        return False

def validar_stock(stock: int) -> bool:
    if stock >=0:
        return True
    else:
        return False

def agregar_juego(codigo: str, titulo: str, plataforma: str, genero: str, clasificacion: str, multiplayer: str, editor: str, precio: int, stock: int, juegos: dict, inventario: dict) -> bool:
    existe = buscar_codigo(codigo, inventario)
    if existe:
        return False
    else:
        juegos[codigo]=[titulo, plataforma, genero, clasificacion, multiplayer, editor]
        inventario[codigo]=[precio, stock]
        return True
    
#--------------------------
#Funcion opcion 5
def eliminar_juego(codigo: str, juegos: dict, inventario: dict) -> bool:
    existe = buscar_codigo(codigo, inventario)
    if existe:
        del juegos[codigo]
        del inventario[codigo]
        return True
    else:
        return False
    
#--------------------------
#Codigo principal
while True:
    system("cls")
    print(juegos)
    print(inventario)
    print("""
    ======== MENÚ PRINCIPAL ========
    1. Stock por plataforma
    2. Búsqueda de juegos por rango de precio
    3. Actualizar precio de juego
    4. Agregar juego
    5. Eliminar juego
    6. Salir
    =================================""")
    
    opcion = leer_opcion()
    
    if opcion == 1:
        plataforma = input("Ingrese plataforma: ").upper()
        stock_plataforma(plataforma, juegos, inventario)
    
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese el precio minimo del rango: "))
                p_max = int(input("Ingrese el precio maximo del rango: "))
                
                if p_min <0 or p_max <0 and p_min > p_max:
                    print("Valores ingresados no validos. Intente nuevamente.")
                else:
                    busqueda_precio(p_min, p_max, juegos, inventario)
                    break
            except ValueError:
                print("Error. Deben ingresarse valores enteros")
                
    elif opcion == 3:
        while True:
            codigo = input("Ingrese codigo del juego: ").upper().strip()
            resultado = validar_codigo(codigo)
            if resultado:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio a registrar: $"))
                    if nuevo_precio >=0:
                        resultado = actualizar_precio(codigo, nuevo_precio, inventario)
                        if resultado:
                            print("El precio fue actualizado de forma correcta.")
                        else:
                            print("El codigo ingresado no se encuentra registrado.")
                        
                        opcion = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                        if opcion == "n":
                            break
                        elif opcion == "s":
                            pass
                        else:
                            print("Solo se permiten valores (s/n).")
                except ValueError:
                    print("El precio ingresado no es valido. Solo se permiten valores enteros.")
            else:
                print("El codigo ingresado no es valido.")
    elif opcion == 4:
        while True:
            codigo = input("Ingrese codigo para registrar: ").upper().strip()
            resultado = validar_codigo(codigo)
            if not resultado:
                print("El codigo ingresado no es valido.")
                break
            
            titulo = input("Ingrese titulo del juego: ").capitalize().strip()
            resultado = validar_titulo(titulo)
            if not resultado:
                print("El titulo ingresado no es valido.")
                break
            
            plataforma = input("Ingrese plataforma: ").upper().strip()
            resultado = validar_plataforma(plataforma)
            if not resultado:
                print("La plataforma ingresada no es valida.")
                break
            
            genero = input("Ingrese genero del juego: ").capitalize().strip()
            resultado = validar_genero(genero)
            if not resultado:
                print("El genero ingresado no es valido.")
                break
            
            clasificacion = input("Ingrese la clasificacion (E/T/M): ").upper().strip()
            resultado = validar_clasificacion(clasificacion)
            if not resultado:
                print("Solo se permiten valores (E/T/M).")
                break
            
            multiplayer = input("¿El juego es multiplayer (s/n)?: ").lower().strip()
            resultado = validar_multiplayer(multiplayer)
            if not resultado:
                print("Solo se permiten valores (s/n).")
                break
            else:
                if multiplayer == "s":
                    multiplayer = True
                else:
                    multiplayer = False
                    
            editor = input("Ingrese editor: ").capitalize().strip()
            resultado = validar_editor(editor)
            if not resultado:
                print("El editor ingresado no es valido.")
                break
            
            try:
                
                precio = int(input("Ingrese precio del juego: $"))
                resultado = validar_precio(precio)
                if not resultado:
                    print("El precio ingresado no es valido.")
                    break
                
                stock = int(input("Ingrese la cantidad de stock del juego: "))
                resultado = validar_stock(stock)
                if not resultado:
                    print("El stock ingresado no es valido.")
                    break
                
                else:
                    resultado = agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario)
                    if resultado:
                        print("El juego ingresado fue registrado correctamente.")
                        break
                    else:
                        print("El codigo ingresado ya se encuentra registrado.")
                        break
                    
            except ValueError:
                print("Error. Solo se permiten valores numericos enteros.")
                break
            
    elif opcion == 5:
        codigo = input("Ingrese el codigo del juego a eliminar: ").upper()
        resultado = eliminar_juego(codigo, juegos, inventario)
        if resultado:
            print("El juego fue eliminado de los registros.")
        else:
            print("El codigo ingresado no se encuentra registrado.")
    elif opcion == 6:
        print("Finalizando programa...")
        exit()
    
    else:
        print("Opcion ingresada no valida. Intente nuevamente.")
    
    input("Presione enter para continuar...")