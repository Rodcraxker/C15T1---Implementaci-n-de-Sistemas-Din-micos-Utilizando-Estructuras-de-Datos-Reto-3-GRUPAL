# CAPA DE ESTRUCTURAS DE DATOS: LISTA ENLAZADA, COLA (FIFO) Y PILA (LIFO)

# 1. LISTA ENLAZADA SIMPLE (Para gestionar el Inventario dinámico de productos)

def crear_lista_enlazada() -> list:
    """
    Inicializa una lista enlazada simple usando un arreglo de 2 posiciones:
    indice 0: referencia al nodo cabeza (None al iniciar)
    indice 1: contador de elementos (0 al iniciar)
    """
    return [None, 0]

def crear_nodo_producto(id_prod: str, nombre: str, cantidad: int, precio: float) -> list:
    """
    Crea un nodo para la lista enlazada representado como un arreglo de 5 posiciones:
    [0: id_prod, 1: nombre, 2: cantidad, 3: precio, 4: puntero_siguiente]
    """
    return [id_prod, nombre, cantidad, round(precio, 2), None]

def insertar_nodo_final(lista_inv: list, id_prod: str, nombre: str, cantidad: int, precio: float) -> None:
    """Inserta un nuevo nodo de producto al final de la lista enlazada."""
    nuevo_nodo = crear_nodo_producto(id_prod, nombre, cantidad, precio)
    if lista_inv[0] is None:
        lista_inv[0] = nuevo_nodo
    else:
        actual = lista_inv[0]
        while actual[4] is not None:
            actual = actual[4]
        actual[4] = nuevo_nodo
    lista_inv[1] += 1

def buscar_nodo_por_id(lista_inv: list, id_prod: str):
    """Recorre la lista enlazada buscando un producto por su ID. Retorna el nodo o None."""
    actual = lista_inv[0]
    while actual is not None:
        if actual[0] == id_prod:
            return actual
        actual = actual[4]
    return None

def eliminar_nodo_por_id(lista_inv: list, id_prod: str):
    """
    Desconecta y elimina un nodo de la lista enlazada según su ID.
    Retorna el nodo eliminado para poder respaldarlo en la Pila de deshacer, o None si no existe.
    """
    actual = lista_inv[0]
    anterior = None
    while actual is not None:
        if actual[0] == id_prod:
            if anterior is None:
                lista_inv[0] = actual[4]
            else:
                anterior[4] = actual[4]
            lista_inv[1] -= 1
            actual[4] = None
            return actual
        anterior = actual
        actual = actual[4]
    return None


# 2. COLA FIFO - FIRST IN, FIRST OUT (Para gestionar Pedidos en orden de llegada)

def crear_cola_pedidos() -> list:
    """Inicializa una cola FIFO respaldada por un arreglo unidimensional."""
    return []

def encolar_pedido(cola: list, id_ped: str, cliente: str, id_prod: str, cantidad: int, tipo_envio: int, total: float) -> None:
    """
    Agrega un pedido al final de la cola (Enqueue).
    Cada pedido es un arreglo: [0: id_ped, 1: cliente, 2: id_prod, 3: cantidad, 4: tipo_envio, 5: total]
    """
    nuevo_pedido = [id_ped, cliente, id_prod, cantidad, tipo_envio, round(total, 2)]
    cola.append(nuevo_pedido)

def desencolar_pedido(cola: list):
    """Extrae y retorna el primer pedido en la fila (Dequeue - índice 0) o None si está vacía."""
    if len(cola) == 0:
        return None
    return cola.pop(0)

def buscar_pedido_en_cola(cola: list, id_ped: str) -> int:
    """Busca un pedido en la cola por su ID y retorna su índice en el arreglo, o -1 si no existe."""
    for i in range(len(cola)):
        if cola[i][0] == id_ped:
            return i
    return -1


# 3. PILA LIFO - LAST IN, FIRST OUT (Para Historial de acciones y función Deshacer)

def crear_pila_historial() -> list:
    """Inicializa una pila LIFO respaldada por un arreglo unidimensional."""
    return []

def apilar_accion(pila: list, tipo_accion: str, descripcion: str, datos_respaldo: list) -> None:
    """
    Inserta una acción en el tope de la pila (Push).
    Cada registro es un arreglo: [0: tipo_accion, 1: descripcion, 2: datos_respaldo]
    """
    pila.append([tipo_accion, descripcion, datos_respaldo])

def desapilar_accion(pila: list):
    """Extrae y retorna la última acción registrada en el tope de la pila (Pop) o None si está vacía."""
    if len(pila) == 0:
        return None
    return pila.pop()