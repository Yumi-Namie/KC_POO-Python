# Funciones para:
# 1. Detectar la presencia de UNA instancia del elelmento dentro de una lista.
# 2. Detectar la presencia de n instancias dentro de una lista, en cualquier posicion.
# . Detectar la presencia de N elelementos SEGUIDOS dentro de una lista.

def find_one(list, needle):
    return find_n( list, needle , 1)

    """
    Devuelve True si encuentra a needle en la lista en alguna posición.
    sino, devuelve False
    """
    """
    # inicializo el contador y el booleano que indica si se cumple o no la condición 
    found = False
    index = 0
    # me recorro la lsta mientras no encuenre a la aguja
    while not found and index < len(list):
        # comprueba a ver si el elemento actual es la aguja
        if needle == list[index]:
            #si lo es, actualizo found
            found = True
        else:
            found = False
        # avanzamos al siguiente elemento
        index = index + 1
    # devolvemos  el resultado
    return found
"""

def find_n(list, needle, n):

    if n > 0:

        # inicializo el contador de veces que lo he encontrado
        # inicializo el indice del elemento actual
        index = 0
        count = 0

        # mientras no haya encontrado n veces y no haya terminado la lista
        #n es el numero de ocurrencias
        while count < n and index < len(list):
            # si la encuentro, actualizo el contador
            if needle == list[index]:
                count = count +1
            # pase lo que pase, actualizo el contador
            index = index +1
        # devuelvo el resultado de comparar n con el contador
        return count >= n

    else:
        return False

def find_streak(list, element , ctde):
    """
    Devuleve True si en list hay ctde o más elementos SEGUIDOS
    False en caso contrario y también si ctde <=0
    """
    if ctde > 0:
        pass
        # Inicializo el indice, el contador, y el indicador de racha
        index = 0
        count = 0
        streak = False #indicador de la racha

        # Mientreas no haya encontrado a ctde de elements seguidos     
        # y la lista no se haya terminado
        while count < ctde and index < len(list):
            if list[index] == element:
                # si lo encuentro, activo el indicador de rachas y incrememnto el contador
                streak = True
                count = count +1
            else:
                # si no lo encuentro, desactivo indicador de rachas y pongo contador a cero
                streak = False
                count = 0
            # avanzo al siguiente elemento (incremento indice)
            index = index +1
        # devolvemos el resultado de comparar el contador con ctde
        # SIEMPRE Y CUANDO ESTEMOS EN RACHA
        if streak == True:
            return count >= ctde
        else:
            return False
    else:
        return False

# buscar una racha de 4s de cantde 3 veces: 4,4,4
# find_streak([0, 7, 7], 7, 3)

def first_elements(list_of_lists):
    """ Recibe una matriz (lista de listas) y devuleve una lista
    con los primeros elementos de cada una de las listas de la matriz

    None | None | None | None
    None | None | None | None
    None | None | None | None
      o  |   o  |   o  |   o  

    """
    return nth_elements(list_of_lists, 0)
    

def nth_elements(list_of_lists,index): #una linea en una columna
    """Recibe una matriz (lista de listas) y devuleve una lista
    con los enesimos elementos de cada una de las listas de la matriz"""
    result = []
    for i in list_of_lists:
        result.append(i[index])
    return result

def transpose(list_of_lists): #todas las lineas en varias columnas (la matriz completa)
    """ Recibe una matriz y devuelve su transpuesta"""
    # creo una matriz vacía, en la que irá acumulando
    matriz_transp = []
    # desde cero al último indice de list_of_lists
    for index in range(len(list_of_lists)): #para cada nº en la lista de: 0,1,2,3
        # extraigo sus valores enésimos y se los encasqueto a la acumlada
        matriz_transp.append(nth_elements(list_of_lists, index))
    # Devulevo la acumulado
    return matriz_transp

def displace (elements, distance):
    """Recibe una lista, y desplaza un elemento pallá.
    Lo que sibra al final, se borra, y el espacio al principio se rellena con None
    [1,2,3,4]---> [None,1,2,3] 
    Desplaza una lista distance a la derecha si distance es positivo y la izqueirda si es negativo
    list slicing()
    "1234"[1:2] >> 2
    "1234"[1:] >> 234 (una lista aprtir de la posic 1)
    """
    res = elements 
    if distance ==0:
        return elements
    elif distance >0:
        filler = [None] * distance #solo se puede concatenar lista con lista
        res = filler + res
        return res[:-distance]#la lista hasta el penultimo
    else:
        # distancia negativa (desplazamos a la izquierda)
        res = res + filler
        return res[abs(distance):] #abs valor absoluto positivas

def displace_matrix(matrix):
    """Desplaza cada una de las listas de la matrix su index-1"""
    #creo una matriz vacía que iré construyendo
    d = []
    #por cada columna de la matriz original, la desplazo indice -1
    for i in range(len(matrix)):
        #añado la columna desplazada a la matriz que estoy construyendo
        d.append(displace(matrix[i], i -1))
    #devulevo la matriz que he contruido
    return d

"""
matrix = [['x','x','o',None], ['x','o',None,None], ['o', None'None'None], [None,None,None,None]]
matrix
[['x','x','o',None]
 ['x','o',None,None]
 ['o', None'None'None]
[None,None,None,None]]

displace_matrix(matrix)
['x','o',None,None]
['x','o',None,None]
[None,'o',None,None]
[None,None,None,None]

"""

def reverse_list(lista):
    # Lo que quiero es una nueva lista con los mismo elementos en orden inverso
    # hay la funcion reversed que devuleve una nueva lista en formato de objeto como map
    return list(reversed(lista))

def reverse_matrix(matrix):
    rm = []
    for columna in matrix:
        rm.append(reverse_list(columna))
    return rm

def replace(elements, predicate, new_value):
    # creamos un acumulador
    new_list = []
    # recorremos la lista original
    for element in elements:
        # si un elemento, pasa el test, lo cambio por el nuevo
        if predicate(element):
            new_list.append(new_value)
        # si no, se queda tal cual
        else:
            new_list.append(element)
    # devulevo el acumulador
    return new_list

def replace_matrix(matrix, predicate, new_element):
    accum = []
    for sublist in matrix:
        accum.append(replace(sublist, predicate,new_element))
    return accum
