from tkinter import N
from linear_board import LinearBoard
from settings import BOARD_SIZE
from reductores import and_all #se pide una lista de bool, hay que transformar 
from list_utils import *

class SquareBoard():
    """"
    Clase que representa un tablero cuadrado

    Método para:
    1. Añadir un carácter (jugar en una columna)
    2. Detectar la victoria de un jugador
    3. Detectar el empate de 2 jugadores
    4. Detectar que el tablero está lleno
    """

    @classmethod
    def fromList(cls, list_of_lists): #(al reves de self, pone cls (clase))
        """ Recibe una lista de listas (una matriz) y devuelve un tablero
        transforma una lista de listas en una lista de Linearboard"""
        columns = []
        for element in list_of_lists:
            columns.append(LinearBoard.fromList(element))
        board = cls()
        board._columns = columns
        return board




    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_SIZE)]
        #lista de la columna multiplicado por el board size
        #está clonado, se crean en el mismo lugar de la memoria...hay que cambiar estas columnas


    def __repr__(self):
        """Muestra una representacion textual del objeto - un tablero"""
        # return matriz transpuesta deste objeto
        # obtengo la representacion como matriz
        matrix = self.as_matrix()
        # le quito lon Nones para poder concatenar, y los sustituyo por '-'
        matrix = replace_matrix(matrix, lambda x: x== None, '-')

        # transpongo la matriz para tener filas en las listas
        transp = transpose(matrix)
        # la invierto
        transp.reverse()
        # genero una cadena con todas esas listas
        tmp = '\n'
        for row in transp:
            for element in row:
                tmp = tmp + '\t' + element
            tmp = tmp + '\n'
        return f'<{self.__class__}: {tmp}>' 

   

    def is_full(self): # podemos hacer con un reduz
        for element in self._columns:
            all_full = True
            for element in self._columns:
                all_full = all_full and element.is_full() # la columna y el cuadro todos está lleno
        """
        [x, x, None, x] = no_lleno
        
        all_full = True

        0. all_full and board.is_full() = True and True
        """

    def add(self, char, index): #meter la ficha
        self._columns[index].add(char)


    def is_victory(self, char):
        """4 tipos de vicotrias: vertical, horiz, diag desc, diago cresc"""
        return (self._any_vertical_victory(char) or self._any_horizontal_victory(char) or 
                self._any_rising_victory(char) or self._any_sinking_victory(char))
        
    

    def as_matrix(self):
        """ Devuelve su representacion ocmo matriz
        return list(map(lambda x: x._column, self._columns))"""

        matrix = []
        for lin_board in self._columns:
            matrix.append(lin_board.as_list())
        return matrix   

    

    def _any_vertical_victory(self,char):
        """
        return reduce(self._columns, False, lambda x,y: x.is_victory() or y.is_victory())
        eso no funcionaria porque un parametro es un bool y otro un n 
        """
        victory = False #valor inofensivo
        for lin_board in self._columns:
            victory = victory or lin_board.is_victory(char)
        return victory

    
    def _any_horizontal_victory(self,char):
        """ Averigua si en el tablero hay una victoria horizontal, 
        rotando el tablero y al tablero resultante, preguntadole si tiene una victoria vertical"""
        # Obtengo la matriz que representa al tablero ACTUAL(self)
        matrix = self.as_matrix()
        # Transpongo esa matriz (o sea,devuelve  una nueva matriz y no altera a la original)
        transp = transpose(matrix)
        # Creo un tablero temporal a partir de esa matriz
        tmp = SquareBoard.fromList(transp)
        # Le pregunto si tiene alguna victoria vertical
        result = tmp._any_vertical_victory(char)
        # Devolvo ese valor
        return result

    def _any_sinking_victory(self,char):
        # Obtener las columnas con la funcion as_matrix (lista de listas)
        matrix = self.as_matrix()
        # le meto un dispalce_matrix en toa la frente
        matrix = displace_matrix(matrix)
        # si había victoria descendente, ahora es horizontal
        # creo un tablero temporal con esa matriz desplazada
        # original, habia un descendente
        tmp = SquareBoard.fromList(matrix)
        return tmp._any_horizontal_victory(char)
        

    def _any_rising_victory(self,char):
        # obtengo la representacion matricial
        matrix = self.as_matrix()
        # invierto la matriz
        matrix = reverse_matrix(matrix)
        # si había victoria ascendente en la original, en 
        # la invertida, la tengo descendente
        # creo un tablero temporal con la invertida
        tmp = SquareBoard.fromList(matrix)
        # miro si hay victoria descendente
        return tmp._any_sinking_victory(char)
        
    


    