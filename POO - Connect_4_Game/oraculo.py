from enum import Enum

class ColumnClassification(Enum):
    # OPCIONES:
    FULL = -1 #PEROR OPCION : IMPOSIBLE JUGAR AHI PORQUE ESTÁ LLENA
    MAYBE = 10 # Puede ser. A saber cómo te vá

class BaseOracle():
    def get_recommensation(self, board, player):
        """" Devuelve lista de recomendaciones (una por columna)"""
        pass

    

