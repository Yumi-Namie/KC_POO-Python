from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2

class Play():
    """
    Representa una jugada
    """
    def description(self):
        pass

   
    def compare(self, otherPlay):
        """ Compara papel con otras jugadas y devuelve un Result"""
        # Si self y otherPlay son iguales, empate
        if self == otherPlay:
            return Result.EQUAL
        # Si otherPlay está en mi beats, le gano yo
        elif otherPlay in self.beats():
            return Result.WINS
        # Sino, gana otherPlay y pierdo yo
        else:
            return Result.LOSES

    # Dunders
    def __eq__(self, other):
        """Devuelve True si self y Other son equivalentes"""
        if isinstance(self,other.__class__):
            #  Tenemos la misma clase o subclase, talvez seamos iguales, vamos a comparar propriedades
            # Mismo sendo de la misma clase, compramos los players si son iguales
            return self.description() == other.description()
        else:
            #  ni en pedo podemos ser iguales
            return False
    def __hash__(self):
        """Devuelve un hash que represente a las propriedades de self"""
        return hash(self.description())


class Paper(Play):
    def beats(self):
        return {Rock(), Spock()}

    def description(self):
        return " Paper🖐 "




class Scissors(Play):
    def beats(self):
        return{Paper(), Lizard()}

    def description(self):
        return " Scissors✌ "
        
    
        

class Rock(Play):
    def beats(self):
        return {Scissors(), Lizard()}

    def description(self):
        return " Rock👊 "

   


class Lizard(Play):
    def beats(self):
        return {Spock(), Paper()}
        """ Devuelve un set conm aquellos plays a los que self derrota"""
        pass


    def description(self):
        return " Lizard🤏 "

  


class Spock(Play):
    def beats(self):
        return {Scissors(), Rock()}

    def description(self):
        return " Spock🖖 "

   


    
            


