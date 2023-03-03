from random import choice 
from play2 import Lizard, Paper, Rock, Scissors, Result, Spock


def run_game():
    """
    Arranca el juego - Start
    """
    display_game() #Mostrar el nombre del juego
    while True:
        user_play = get_user_play() # Jugada de lusuario
        comp_play = random_play() #Jugada del ordenador al azar
        display_match(user_play, comp_play)

        winner = get_winner(user_play, comp_play) # hay que compararlas: vencedor o ampate
        if winner == None: # empate
            display_tie(user_play, comp_play) # Mostra empate
        else:
            display_victory(winner)
        resp = another_match()
        if resp == False:      
            break
        

                                                                      

def display_game():
    """Muestra el nombre del juego"""
    print("\n\n\t\t >>> Rock - Paper - Scissors - Lizard - Spock <<< \n\n")

def display_match(play1,play2):
    print(f'{play1.description()} vs {play2.description()} \n\n⚔️  FIGHT! ⚔️\n')

def get_user_play():
    """ Le pregunta al usuario qué quieres jugar y lo devuelve"""
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    elif res ==3:
        return Scissors()
    elif res ==4:
        return Lizard()
    else:
        return Spock()

def get_user_response():
    """Presenta un menu de opciones y pide que seleccione una.
    Devuelve una <cadena> que indica lo ha elegido"""
    response = None
    while True:
        print("Chose your play:")
        print("1. Rock  👊")
        print("2. Paper 🖐")
        print("3. Scissors ✌")
        print("4. Lizard 🤏")
        print("5. Spock 🖖")


        raw = input("Enter 1, 2, 3, 4 o 5\n")
        #validar raw
        raw = raw.strip()
        if raw == "1":
            response = 1
            break
        elif raw == "2":
            response = 2
            break
        elif raw == "3":
            response = 3
            break
        elif raw == "4":
            response = 4
            break
        elif raw == "5":
            response = 5
            break
        else:
            continue #sigue dando el while
    return response

def random_play():
    """ Selecciona una jugada al azar para competir con el usuario"""
    return choice([Paper(), Rock(), Scissors(), Lizard(), Spock()])

def get_winner(play1, play2):
    """ Comparar las dos jugadas: Obtiene el vencedor o None si hay empate"""
   
    result = play1.compare(play2)
    if result == Result.WINS:
        winner = play1
    elif result == Result.LOSES:
        winner = play2
    else:
        winner = None
    return winner



def display_tie(play1, play2):
    """ Imprime que ha habido un empate"""
    if type(play1) == type(play2):
        print(f'🤦 Empate entre dos {play1.description()}')
    
def display_victory(winner):
    """ Muestra que winner ha ganado"""
    print(f'🎉 Ha ganado {winner.description()}!! ')
   

def another_match():
    """ Preguntar al jugador si quiere una partida más"""
    while True:
        print("\n\nQuieres jugar nuevamente? (S/N)")
        response = input("Enter S o N \n")
        #Validar raw
        response = (response.upper()).strip()
        if response == "S":
            return True
        elif response == "N":
            print(choice(["¿Eres un gallina, McFly 🐓?", "¡Cobarde! 😏", "Vete a llorar! 😭"]))
            return False
        else:
            continue



if __name__ == '__main__':
    run_game()




