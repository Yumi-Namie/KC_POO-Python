from settings import BOARD_SIZE, VICTORY_STRIKE
from list_utils import find_streak


class LinearBoard:
    
    """
    Representa un tablero tenga un tamaõ 'fijo' con una sola columna.
    x representa al jugador 1
    o representa al jugador 2
    None representa un espacio vacío
    """
    @classmethod
    def fromList(cls, list):
        """ Crea y devolve un Linearboard a partir de una lista que representa una jugada"""
        board = cls() # una variable de una clase = LinearBoard()
        board._column = list
        return board

    

        

    def __init__(self):
        """
        Inicializa el tablero vacío. usease, lleno de None
        """
        #self._column = [None] * BOARD_SIZE #[None, None, None, None] privado se puede hacer con dos guion bajo o solo una (menos importante)
        self._column = [None for i in range (BOARD_SIZE)]

    def is_full(self):
        """
        Devuelve True si el tablero está lleno
        """
        # si el ultimo elemento es None, no está lleno (full)
        if self._column[-1] == None:
            return False
        else:
            return True


    def as_list(self):
        """ Devuleve la representación del tablero como una lista"""
        return self._column     


    def add(self,char): #añadir fichas de los jugadores x y o (char+character)
        """
        Añade una 'ficha' en dicha columna, en el primer espacio disponible
        Cuando encuentre un None, meto un char
        """

        # si no está lleno
        if not self._is_full():

            #averiguo donde está el primer None
            i = self._column.index(None)

            # lo cambio por un char
            self._column[i] = char
        pass

    def is_victory(self,char): # quien es el gañador?
        return find_streak(self.column, char, VICTORY_STRIKE)

    def is_tie(self, char1, char2): #es empate?
        # si no hay victoria e nadie, pues hay empate
        if (self.is_victory(char1) == False) and (self.is_victory(char2) == False) and self.is_full():
            return True
        else:
            return False