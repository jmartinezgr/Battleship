import random
import time
import os
import pprint

def mainMenu():
    print("----- Nombre_grupo -----")
    print("----- Batalla Naval -----")
    print("----- Menú Principal -----")
    print("1. Introducir nombre del jugador.")
    print("2. Iniciar juego.")
    print("3. Cerrar programa.")

def showBoard(pjBoard, pcBoard,usr_name = "PJ"):
    
    if usr_name is not None:
        ancho = 10 if len(usr_name) <= 8 else len(usr_name) + 2
    else:
        ancho = 10

    print("PC".center(ancho,'='))
    for row in pcBoard:
        print("".join([
            item if item != 'B' else 'O' for item in row  
        ]))
    print("==========")
    print(usr_name.center(ancho,'='))
    for row in pjBoard:
        print("".join(row))
    print("==========")

def initializeBoards():
    return [['O' for _ in range(10)] for _ in range(10)]

def placeShips(board, numShips, pc = False):
    shipsPlaced = 0
    while shipsPlaced < numShips:
        try:
            if not pc:
                row = int(input(f"Ingrese la fila para su barco {shipsPlaced+1}: "))
                col = int(input(f"Ingrese la columna para su barco {shipsPlaced+1}: "))
            else:
                row = random.randint(0,9)
                col = random.randint(0,9)
            if board[row-1][col-1] == 'O':
                board[row-1][col-1] = 'B'
                shipsPlaced += 1
                os.system('cls')
            else:
                print("Seleccione otra ubicación.") if not pc else None
        except (ValueError, IndexError):
            os.system('cls')
            print("Entrada inválida. Inténtelo de nuevo.")
    return board

def playerTurn(pjBoard, pcBoard):
    print()
    print(''.center(50, '='))
    while True:
        try:
            row = input("Ingrese la fila para su disparo: ")
            col = input("Ingrese la columna para su disparo: ")

            # Verificar si la coordenada es 'X'
            if row.upper() == 'X' or col.upper() == 'X':
                print("Coordenada no válida. No puedes usar 'X'. Inténtelo de nuevo.")
                continue  # Reiniciar el bucle para solicitar otra vez la entrada

            row = int(row)
            col = int(col)

            print("Se esta verificando si el ataque fue exitoso", end='', flush=True)

            for _ in range(3):  # Repetir tres veces para mostrar puntos, luego dos puntos, luego uno.
                time.sleep(0.5)  # Pausa para dar un efecto visual gradual.
                print(".", end='', flush=True)

            print()  # Nueva línea después de los puntos

            if pcBoard[row - 1][col - 1] == 'B':
                print("Impacto!")
                pcBoard[row - 1][col - 1] = 'D'
            else:
                print("Disparo Fallado!")
                pcBoard[row - 1][col - 1] = 'X'
            break
        except (ValueError, IndexError):
            print("Entrada inválida. Inténtelo de nuevo.")


def computerTurn(pjBoard, pcBoard):
    print("La máquina está eligiendo donde disparar ", end='', flush=True)
    
    for _ in range(3):  # Repetir tres veces para mostrar puntos, luego dos puntos, luego uno.
        time.sleep(0.5)  # Pausa para dar un efecto visual gradual.
        print(".", end='', flush=True)

    print()  # Nueva línea después de los puntos

    while True:
        time.sleep(1)  # Pausa para dar un efecto visual antes de mostrar el mensaje final.

        row = random.randint(0, 9)
        col = random.randint(0, 9)

        if pjBoard[row][col] == 'B':
            print("Impacto Enemigo")
            pjBoard[row][col] = 'D'
        elif pjBoard[row][col] == 'O':
            print("Disparo Enemigo Fallado")
            pjBoard[row-1][col-1] = 'X'
            break
    
    print(''.center(50,'='))

def game_over(board):
    for row in board:
        if 'B' in row:
            return False
    return True

def playGame(player_name):
    pjBoard = initializeBoards()
    pcBoard = initializeBoards()

    os.system('cls')
    pjBoard = placeShips(pjBoard, 2)
    os.system('cls')
    pcBoard = placeShips(pcBoard, 1,True)

    pprint.pprint(pcBoard)
    
    time.sleep(10)
    
    os.system('cls')
    print('Juego Iniciado'.center(20,'='))
    print()
    time.sleep(1.5)
    while True:
        showBoard(pjBoard, pcBoard,player_name) if player_name != '' else showBoard(pjBoard, pcBoard)
        playerTurn(pjBoard, pcBoard)
        if game_over(pcBoard):
            os.system('cls')
            print("Juego Terminado.") 
            print("El ganador es: PJ") if player_name == '' else print(f'Juego Terminado. El ganador es : {player_name}')
            input("Presione Enter para volver al menú inicial.")
            break
        print(''.center(50,'='))
        #showBoard(pjBoard, pcBoard,player_name) if player_name != '' else showBoard(pjBoard, pcBoard,player_name)
        computerTurn(pjBoard, pcBoard)
        time.sleep(3)
        print()
        if game_over(pjBoard):
            os.system('cls')
            print("Juego Terminado.")
            print("El ganador es: PC")
            input("Presione Enter para volver al menú inicial.")
            break
# Función principal
def main():
    player_name = ''
    while True:
        mainMenu()
        option = input("Ingrese el número de la opción: ")

        if option == '1':
            player_name = input("Ingrese su nombre: ")
            print("Hola", player_name)
            os.system('cls')
        elif option == '2':
            playGame(player_name)
            os.system('cls')
        elif option == '3':
            print("Fin del Programa.")
            break
        else:
            print("ERROR: Selección Inválida")

if __name__ == "__main__":
    main()