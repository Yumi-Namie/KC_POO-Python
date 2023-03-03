# reductoras - coge una lista y reducir a un total 
class Coin:

    def __init__ (self, amount):
        self.amount = amount

class Switch:
    def __init__ (self, state):
        self.state = state
                

def sum_all(numbers):
    """
    Recibe una suma de números y los combina (mediante +)
    a uno solo, que será el total
    """ 
    total_so_far = 0 #tenemos que indicar un numero para poder sumar, si fuera multiplicar seria 1
    for element in numbers:
        total_so_far = total_so_far + element
    return total_so_far

def mult_all(numbers):
    """
    Recibe una lista de númeris y la reduce a uno solo
    """
    total_so_far = 1
    for element in numbers:
        total_so_far = total_so_far * element
    return total_so_far

def concat_all(strings):
    """
    Recibe lista de cadenas y las reduce a una sola 
    concatenandolas
    """

    total_so_far = ""
    for element in strings:
        total_so_far = total_so_far + element
    return total_so_far

def and_all(bools):
    """
    Reduce una lista de booleanos a uno solo, usando el and
    """   
    total_so_far = True

    for element in bools:
        total_so_far = total_so_far and element
    return total_so_far


def or_all(bools):
    total_so_far = True
    for element in bools:
        total_so_far = total_so_far or element
    return total_so_far



